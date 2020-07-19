from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Risk Management"),
			"items": [
				{
					"type": "doctype",
					"name": "risk",
					"onboard": 1,
				},
				
			]
		}
		
	]
