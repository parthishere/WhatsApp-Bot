from .serializers import UserSerializer, UserProfileSerializer
from whatsapp_app.models import User, UserProfile

from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse

response = MessagingResponse()
message = Message()
message.body('Hello World!')
response.append(message)