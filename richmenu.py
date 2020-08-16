# -*- coding: utf-8 -*-

""" Rich Menu Manager for Line Messaging API """
import json
import requests

class RichMenu:
    """ Datamodel of RichMenu """
    def __init__(self, name, chat_bar_text, size_full=True, selected=False):
        """
        :param name: Name of this RichMenu
        :type name: str
        :param chat_bar_text: Text on the menu label
        :type chat_bar_text: str
        :param size_full: Full size menu
        :type size_full: bool
        :param selected: Open when the conversation starts
        :type selected: bool
        """
        self.size = {"width": 2500, "height": 1686}
        if not size_full:
            self.size["height"] = 843
        self.selected = selected
        self.name = name
        self.chat_bar_text = chat_bar_text
        self.areas = []

    def add_area(self, x, y, width, height, action_type, payload):
        """ Add an area with action
        :param x: Left position
        :type x: int
        :param y: Top position
        :type y: int
        :param width: Width
        :type width: int
        :param height: Height
        :type height: int
        :param action_type: message / uri / postback
        :type action_type: str
        :param payload: data to pass
        :type payload: str
        """
        bounds = {"x": x, "y": y, "width": width, "height": height}
        action = {"type": action_type}
        if action_type == "postback":
            if isinstance(payload, list):
                action["data"] = payload[0]
                if len(payload) > 1:
                    action["text"] = payload[1]
            else:
                action["data"] = payload
        elif action_type == "uri":
            action["uri"] = payload
        else:
            action["text"] = payload
        self.areas.append({"bounds": bounds, "action": action})

    def to_json(self):
        """ Convert to JSON
        :return Json serialized string of this Rich menu
        :rtype: str
        """
        dic = {"size": self.size, "selected": self.selected, "name": self.name, "chatBarText": self.chat_bar_text, "areas": self.areas}
        return json.dumps(dic)

class RichMenuManager:
    """ RichMenu Manager """
    def __init__(self, channel_access_token, verify=True):
        """
        :param channel_access_token: Channel Access Token
        :type channel_access_token: str
        :param verify: Verify SSL
        :type verify: bool
        """
        self.headers = {"Authorization": "Bearer {%s}" % channel_access_token}
        self.verify = verify

    def register(self, rich_menu, image_path=None):
        """ Register RichMenu
        :param rich_menu: RichMenu to register
        :type rich_menu: RichMenu
        :param image_path: File path of the image
        :type image_path: str
        """
        url = "https://api.line.me/v2/bot/richmenu"
        res = requests.post(url, headers=dict(self.headers, **{"content-type": "application/json"}), data=rich_menu.to_json(), verify=self.verify).json()
        if image_path:
            test = self.upload_image(res["richMenuId"], image_path)
        return res

    def upload_image(self, rich_menu_id, image_path):
        """ Upload image of specific RichMenu
        :param rich_menu_id: ID of the RichMenu to upload image for
        :type rich_menu_id: str
        :param image_path: File path of the image
        :type image_path: str
        """
        url = "https://api.line.me/v2/bot/richmenu/%s/content" % rich_menu_id
        image_file = open(image_path, "rb")
        # image_file = image_path
        # image_file = cloudstorage.open(image_path, mode='rb')
        return requests.post(url, headers=dict(self.headers, **{"content-type": "image/png"}), data=image_file, verify=self.verify).json()

    def download_image(self, richmenu_id, filename=None):
        """ Download image of specific RichMenu
        :param rich_menu_id: ID of the RichMenu
        :type rich_menu_id: str
        :param filename: File path to save the image
        :type filename: str
        :return image: Binary data of menu image
        """
        url = "https://api.line.me/v2/bot/richmenu/%s/content" % richmenu_id
        res = requests.get(url, headers=self.headers, verify=self.verify)
        if filename:
            with open(filename, "wb") as f:
                f.write(res.content)
        else:
            return res.content

    def get_list(self):
        """ Get all RichMenus
        :return : All Richmenu as JSON
        :rtype : dict
        """
        url = "https://api.line.me/v2/bot/richmenu/list"
        return requests.get(url, headers=self.headers, verify=self.verify).json()

    def remove(self, richmenu_id):
        """ Remove Richmenu
        :param rich_menu_id: ID of the RichMenu to remove
        :type rich_menu_id: str
        """
        url = "https://api.line.me/v2/bot/richmenu/%s" % richmenu_id
        return requests.delete(url, headers=self.headers, verify=self.verify).json()


    def remove_all(self):
        """ Remove all RichMenus """
        menus = self.get_list()
        for m in menus["richmenus"]:
            self.remove(m["richMenuId"])

    def apply(self, user_id, richmenu_id):
        """ Apply RichMenu to user
        :param user_id: UserID to apply RichMenu
        :type user_id: str
        :param rich_menu_id: ID of the RichMenu
        :type rich_menu_id: str
        """
        url = "https://api.line.me/v2/bot/user/%s/richmenu/%s" % (user_id, richmenu_id)
        return requests.post(url, headers=self.headers, verify=self.verify).json()

    def detach(self, user_id):
        """ Detach RichMenu from user
        :param user_id: UserID to detach custom RichMenu
        :type user_id: str
        """
        url = "https://api.line.me/v2/bot/user/%s/richmenu" % user_id
        return requests.delete(url, headers=self.headers, verify=self.verify).json()

    def get_applied_menu(self, user_id):
        """ Get applied RichMenu to specific user
        :param user_id: UserID to get applied RichMenu
        :type user_id: str
        """
        url = "https://api.line.me/v2/bot/user/%s/richmenu" % user_id
        return requests.get(url, headers=self.headers, verify=self.verify).json()
