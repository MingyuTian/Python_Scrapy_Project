# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class OkCorpItem(Item):
	url = Field()
	businessName = Field()
	addressRegion = Field()
	category = Field()
	status = Field()
	registeredAgentState = Field()
	dateOfIncorporation = Field()
	registeredAgentName = Field()
	registeredAgentAddress = Field()
	registeredAgentCity = Field()
	registeredAgentZip = Field()
	registeredAgentAddressFormat = Field()
	ubi = Field()
	name_type = Field()
	pass
