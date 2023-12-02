from .forms import ContactForm

def contact_form_context(request):
    return {
        'contact_form' : ContactForm()
    }