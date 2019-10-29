import os
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.labels',
    'https://www.googleapis.com/auth/gmail.modify'
]

def sender_string():
    senders = [
        'from:amazon.in', 
        'from:youtube.com',
        'from:linkedin.com',
        'from:facebook.com',
        'from:promo.payback.in',
        'from:meetup.com',
        'from:airasia.com',
        'from:adzuna.com',
        'from:noreply-photos@google.com',
        'from:paytm.com',
        'from:resume@shinecareers.com',
        'from:edm.konnectmail.com',
        'from:investmails.in',
        'from:guru.com',
        'from:getsimpl.com',
        'from:gitter.im',
        'from:jobalert@timesjobs.com',
        'from:info@hirist.com',
        'from:urbanpro-no-reply@urbanpro.com',
        'from:noreply@medium.com',
        'from:techgig.com',
        'from:redditmail.com',
        'from:learnpick.in',
        'from:email.udemy.com',
        'from:instagram.com',
        'from:cleverprogrammer.com',
        'from:info@communitymatrimony.com',
        'from:service.axisbankmail.com',
        'from:info@realpython.com',
        'from:baj.bajajfinserv-markets.in',
        'from:upgrad.com',
        'from:inoxmovies.com',
        'from:bigbasket.in',
        'from:olamoney.com',
        'from:mail@mail.adobe.com',
        'from:updates@info.sbicreditcard.com',
        'from:voxcinemas.com',
        'from:notifications@ixigo.com',
        'from:spicejet@web-spicejet.com',
        'from:iimjobs.com',
        'from:updates.freelancer.com',
        'from:do-not-reply@stackoverflow.email',
        'from:jobs@jobs.shine.com',
        'from:emailjobdelivery.com',
        'from:facebookmail.com',
        'from:mailrobot@internations.org',
        'from:letters@medium.com',
        'from:swiggy.in',
        'from:no-reply@entertainment.bookmyshow.com',
        'from:noreply@notifications.freelancer.com',
        'from:edureka.co',
        'from:mailclues.info',
        'from:tickets@bookmyshow.email',
        'from:zomato.com',
        'from:customer.communication@axisbank.in',
        'from:notifications@content.goibibo.com',
        'from:uber.com',
        'from:noreply@notifications.freelancer.com',
        'from:pvrcinemas.com',
        'from:udacity.com',
        'from:myntra.com',
        'from:nl.jabong.com',
        'from:innerengineering.com',
        'from:expediamail.com',
        'from:zoom.us',
        'from:m.mail.coursera.org',
        'from:qemailserver.com',
        'from:wesbos.com',
        'from:alerts.hotstar.com',
        'from:pbmails.payback.in',
        'from:naukrigulf.com',
        'from:mail.tradingacademy.com',
        'from:codecademy.com',
        'from:olacabs.com',
        'from:personalcapital.com',
        'from:e.feedspot.com',
        'from:eduonix.com',
        'from:eduonixmail.com'
        'from:naukri.com',
        'from:quora.com',
        'from:timesjobsmailer.in',
        'from:mail.open.mit.edu',
        'from:primevideo.com',
        'from:nsdl.co.in',
        'from:emailjobdelivery.com',
        'from:twitter.com',
        'from:phonepe.com',
        'from:e.etsy.com',
        'from:packtpub.com',
        'from:timesjobs.com',
        'from:tumblr.com',
        'from:crm.ajiolife.in',
        'from:pbmail.payback.in',
        'from:zestmoney.in',
        'from:ishafoundation.org',
        'from:codementor.io',
        'from:fcemail.in',
        'from:ishausa.org',
        'from:campaign.journey.cloud',
        'from:mailer.abhibus.com',
        'from:tapatalk.com',
        'from:lazypay.in',
        'from:mail.blinkist.com',
        'from:alerts.shine.com',
        'from:donotreply@intel.com',
        'from:urbanpro-no-reply@urbanpro.com',
        'from:promos.payback.in',
    ]
    return ' '.join(senders)

creds = None

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

# build the Service point to access

service = build('gmail', 'v1', credentials = creds)

def get_marker_lbl():
    # for lbl in service.users().labels().list(userId='me').execute()['labels']:
    #     print(lbl['name'])
    return [lbl['id'] for lbl in service.users().labels().list(userId='me').execute()['labels'] if lbl['name'] == 'INBOX'][-1]

def main():
    senders = {sender_string()}
    query = f'{senders}'
    # print(query)
    
    message_loader = service.users().messages()
    marker_label_id = get_marker_lbl()

    while True:
        mails = message_loader.list(userId='me', q=query).execute()
        if 'messages' not in mails:
            print('No Emails to Process')
            return 'Done'
        
        print('Moving {} mails to Trash'.format(len(mails['messages'])))

        for mail in mails['messages']:
            message_loader.trash(userId='me', id=mail['id']).execute()
            # print(mail['id'])
        
    return 'Done'

if __name__ == '__main__':
    main()