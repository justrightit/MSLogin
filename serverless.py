from flask import Flask, request, send_file

##if Teams webhook alerting wanted - uncomment below :
import pymsteams
myTeamsMessage = pymsteams.connectorcard("https://justrightit.webhook.office.com/webhookb2/f0f7e432-2afe-4ad3-918b-f74fa7ac699d@73cd84de-4fe8-433d-87c1-6d323558f6f0/IncomingWebhook/42f37aeab4dc48029956bf660b8aaeaf/0f4871ef-9f5c-4e8e-83af-d862bb27de20/V2sIiQnmElFSNqWq2rIz9IXA2OnAMPTDFCXoV82oC42Fk1") #replace with Teams Webhook URL

global filename = "warning.png" #Debug
allowed_referers = [
        'login.microsoftonline.com',
        'login.microsoft.net',
        'login.microsoft.com',
        'autologon.microsoftazuread-sso.com',
        'tasks.office.com',
        'login.windows.net']
app = Flask(__name__)

@app.route('/companyBranding.png', methods=['GET'])
def pixel():
    referer_header = str(request.headers.get('Referer'))   
    referer_header = referer_header.replace("https://","").replace("/","")
    if (referer_header not in allowed_referers) and (referer_header is not None) and (len(referer_header) > 1):
        print(f"[!] Non-Microsoft referer header detected: {referer_header}")
        print(f"[*] Referer header (AitM): {referer_header}")
        #requester_ip = request.remote_addr  #To fix.
        #print(f"[*] Requester IP (user logging in): {requester_ip}")    #To Fix.
        #Teams Webhook#
        #myTeamsMessage.text(f"[*] Referer header (AitM): {referer_header}")
        #myTeamsMessage.send()  
        return send_file('warning.png', mimetype='image/png',as_attachment=False)
    else:
        return send_file('safe.png', mimetype='image/png',as_attachment=False) 

def main():
        app.run(debug=True)

if __name__ == "__main__":
    main()
