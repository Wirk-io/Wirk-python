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


class AppReaderServiceModel(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AppReaderServiceModel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'app_name': 'str',
            'has_instruction': 'bool',
            'has_question_options': 'bool',
            'id_app': 'int',
            'qualities': 'list[QualityReaderServiceModel]',
            'title_question_options': 'str'
        }

        self.attribute_map = {
            'app_name': 'AppName',
            'has_instruction': 'HasInstruction',
            'has_question_options': 'HasQuestionOptions',
            'id_app': 'IdApp',
            'qualities': 'Qualities',
            'title_question_options': 'TitleQuestionOptions'
        }

        self._app_name = None
        self._has_instruction = None
        self._has_question_options = None
        self._id_app = None
        self._qualities = None
        self._title_question_options = None

    @property
    def app_name(self):
        """
        Gets the app_name of this AppReaderServiceModel.


        :return: The app_name of this AppReaderServiceModel.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """
        Sets the app_name of this AppReaderServiceModel.


        :param app_name: The app_name of this AppReaderServiceModel.
        :type: str
        """
        self._app_name = app_name

    @property
    def has_instruction(self):
        """
        Gets the has_instruction of this AppReaderServiceModel.


        :return: The has_instruction of this AppReaderServiceModel.
        :rtype: bool
        """
        return self._has_instruction

    @has_instruction.setter
    def has_instruction(self, has_instruction):
        """
        Sets the has_instruction of this AppReaderServiceModel.


        :param has_instruction: The has_instruction of this AppReaderServiceModel.
        :type: bool
        """
        self._has_instruction = has_instruction

    @property
    def has_question_options(self):
        """
        Gets the has_question_options of this AppReaderServiceModel.


        :return: The has_question_options of this AppReaderServiceModel.
        :rtype: bool
        """
        return self._has_question_options

    @has_question_options.setter
    def has_question_options(self, has_question_options):
        """
        Sets the has_question_options of this AppReaderServiceModel.


        :param has_question_options: The has_question_options of this AppReaderServiceModel.
        :type: bool
        """
        self._has_question_options = has_question_options

    @property
    def id_app(self):
        """
        Gets the id_app of this AppReaderServiceModel.


        :return: The id_app of this AppReaderServiceModel.
        :rtype: int
        """
        return self._id_app

    @id_app.setter
    def id_app(self, id_app):
        """
        Sets the id_app of this AppReaderServiceModel.


        :param id_app: The id_app of this AppReaderServiceModel.
        :type: int
        """
        self._id_app = id_app

    @property
    def qualities(self):
        """
        Gets the qualities of this AppReaderServiceModel.


        :return: The qualities of this AppReaderServiceModel.
        :rtype: list[QualityReaderServiceModel]
        """
        return self._qualities

    @qualities.setter
    def qualities(self, qualities):
        """
        Sets the qualities of this AppReaderServiceModel.


        :param qualities: The qualities of this AppReaderServiceModel.
        :type: list[QualityReaderServiceModel]
        """
        self._qualities = qualities

    @property
    def title_question_options(self):
        """
        Gets the title_question_options of this AppReaderServiceModel.


        :return: The title_question_options of this AppReaderServiceModel.
        :rtype: str
        """
        return self._title_question_options

    @title_question_options.setter
    def title_question_options(self, title_question_options):
        """
        Sets the title_question_options of this AppReaderServiceModel.


        :param title_question_options: The title_question_options of this AppReaderServiceModel.
        :type: str
        """
        self._title_question_options = title_question_options

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

