import gdata


from gdata.spreadsheet.service import SpreadsheetsService

key = '0AlZH8QBl60oodEJTdFA5TlZOcDJCMU02RkZoSHF5SHc'

client = SpreadsheetsService()
feed = client.GetWorksheetsFeed(key, visibility='public', projection='basic')

# spreadsheet_id = feed.entry[0].id.text.rsplit('/',1)[1]
# feed = gd_client.GetWorksheetsFeed(spreadsheet_id)
# worksheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

# rows = gd_client.GetListFeed(spreadsheet_id, worksheet_id).entry

# for row in rows:
#     for key in row.custom:
#         print " %s: %s" % (key, row.custom[key].text)
#     print


# print feed 

# for sheet in feed.entry:
#   print sheet.title.text

sheet_key = "od6"
print "let's try it!"
data = client.GetListFeed(key, sheet_key, visibility='public', projection='values').entry[0].custom
print data
# rows = gd_client.GetListFeed(spreadsheet_id, worksheet_id).entry