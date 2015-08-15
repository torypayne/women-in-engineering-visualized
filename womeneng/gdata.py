import gdata


from gdata.spreadsheet.service import SpreadsheetsService

key = '0AlZH8QBl60oodEJTdFA5TlZOcDJCMU02RkZoSHF5SHc'

client = SpreadsheetsService()
feed = client.GetWorksheetsFeed(key, visibility='public', projection='basic')



sheet_key = "od6"
print "let's try it!"
data = client.GetListFeed(key, sheet_key, visibility='public', projection='values').entry[0].custom
print data