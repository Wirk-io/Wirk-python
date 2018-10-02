# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class AppProjectWriterServiceModel(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AppProjectWriterServiceModel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_app': 'int',
            'id_quality': 'int',
            'instruction': 'str',
            'question_options': 'list[str]',
            'title': 'str',
            'url_notification': 'str'
        }

        self.attribute_map = {
            'id_app': 'IdApp',
            'id_quality': 'IdQuality',
            'instruction': 'Instruction',
            'question_options': 'QuestionOptions',
            'title': 'Title',
            'url_notification': 'UrlNotification'
        }

        self._id_app = None
        self._id_quality = None
        self._instruction = None
        self._question_options = None
        self._title = None
        self._url_notification = None

    @property
    def id_app(self):
        """
        Gets the id_app of this AppProjectWriterServiceModel.


        :return: The id_app of this AppProjectWriterServiceModel.
        :rtype: int
        """
        return self._id_app

    @id_app.setter
    def id_app(self, id_app):
        """
        Sets the id_app of this AppProjectWriterServiceModel.


        :param id_app: The id_app of this AppProjectWriterServiceModel.
        :type: int
        """
        self._id_app = id_app

    @property
    def id_quality(self):
        """
        Gets the id_quality of this AppProjectWriterServiceModel.


        :return: The id_quality of this AppProjectWriterServiceModel.
        :rtype: int
        """
        return self._id_quality

    @id_quality.setter
    def id_quality(self, id_quality):
        """
        Sets the id_quality of this AppProjectWriterServiceModel.


        :param id_quality: The id_quality of this AppProjectWriterServiceModel.
        :type: int
        """
        self._id_quality = id_quality

    @property
    def instruction(self):
        """
        Gets the instruction of this AppProjectWriterServiceModel.


        :return: The instruction of this AppProjectWriterServiceModel.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        """
        Sets the instruction of this AppProjectWriterServiceModel.


        :param instruction: The instruction of this AppProjectWriterServiceModel.
        :type: str
        """
        self._instruction = instruction

    @property
    def question_options(self):
        """
        Gets the question_options of this AppProjectWriterServiceModel.


        :return: The question_options of this AppProjectWriterServiceModel.
        :rtype: list[str]
        """
        return self._question_options

    @question_options.setter
    def question_options(self, question_options):
        """
        Sets the question_options of this AppProjectWriterServiceModel.


        :param question_options: The question_options of this AppProjectWriterServiceModel.
        :type: list[str]
        """
        self._question_options = question_options

    @property
    def title(self):
        """
        Gets the title of this AppProjectWriterServiceModel.


        :return: The title of this AppProjectWriterServiceModel.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this AppProjectWriterServiceModel.


        :param title: The title of this AppProjectWriterServiceModel.
        :type: str
        """
        self._title = title

    @property
    def url_notification(self):
        """
        Gets the url_notification of this AppProjectWriterServiceModel.


        :return: The url_notification of this AppProjectWriterServiceModel.
        :rtype: str
        """
        return self._url_notification

    @url_notification.setter
    def url_notification(self, url_notification):
        """
        Sets the url_notification of this AppProjectWriterServiceModel.


        :param url_notification: The url_notification of this AppProjectWriterServiceModel.
        :type: str
        """
        self._url_notification = url_notification

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other
