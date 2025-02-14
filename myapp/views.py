from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import PageContent
from django.db.models import Q
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from .models import Notification

# Create your views here.

def home(request):
    notifications = Notification.objects.all().order_by('-created_at')  # Retrieve all notifications
    return render(request, 'index.html', {'notifications': notifications})

def about(request):
    return render(request, 'about.html')

def areas(request):
    return render(request, 'areas.html')

def facilities(request):
    return render(request, 'Facilities.html')

def opportunity(request):
    return render(request, 'opportunities.html')

def teams(request):
    return render(request, 'Teams.html')

def gallery(request):
    return render(request, 'Gallery.html')

def mgu(request):
    return render(request, 'mgu_page.html')

def form(request):
    return render(request, 'Forms.html')

def dr(request):
    return render(request, 'about_radhakrishnan.html')



#search-------------------------------------------------------------------------------------------------------


def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Searching in both title and body
        results = PageContent.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search_results.html', context)

def page_detail(request, pk):
    page = get_object_or_404(PageContent, pk=pk)
    return render(request, 'page_detail.html', {'page': page})


#forms----------------------------------------------------------------------------------



def submit(request):
    if request.method == "POST":
        # Extract form data
        name = request.POST.get('name')  # Adjust these based on your form fields
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        applyingfor = request.POST.get('applyingFor')
        periodgroup = request.POST.get('period')
        affiliation = request.POST.get('affiliation')
        courseSubject = request.POST.get('courseSubject')
        fromDate = request.POST.get('fromDate')
        toDate = request.POST.get('toDate')

        # Step 1: Load credentials from the JSON file
        creds = Credentials.from_service_account_file('credentials/google_sheets_key.json')

        # Step 2: Connect to the Google Sheets API
        service = build('sheets', 'v4', credentials=creds)

        # Step 3: Specify your Google Sheet ID and range
        spreadsheet_id = '12eNxk-1D5GvrHKBXS_LdNXBr-DB-R1HiPBOYKZeMFCI'  # Replace with your Google Sheet ID
        range_name = 'Sheet1!A1:I1'  # Adjust based on your Google Sheet

        # Step 4: Check if the sheet already has headings
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        existing_data = result.get('values', [])

        # Add headings if the sheet is empty
        if not existing_data:
            headings = [['Name', 'Email', 'Mobile', 'Applying For', 'Period (Months)', 'Affiliation', 'Course Subject', 'From Date', 'To Date']]
            service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption='RAW',
                body={'values': headings}
            ).execute()

        # Step 5: Prepare data to append
        values = [[name, email, mobile, applyingfor, periodgroup, affiliation, courseSubject, fromDate, toDate]]
        body = {'values': values}

        # Step 6: Append the data to the sheet
        service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range='Sheet1!A2:I2',  # Start appending from the second row
            valueInputOption='RAW',
            body=body
        ).execute()

        return render(request, 'form_success.html')
    else:
        return render(request, 'error.html')
    
#-----Notifications------------------------------------------------------------------------------------

def landing_page(request):
    notifications = Notification.objects.all().order_by('-created_at')  # Retrieve all notifications
    return render(request, 'landing_page.html', {'notifications': notifications})