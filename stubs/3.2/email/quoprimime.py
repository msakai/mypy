# Stubs for email.quoprimime (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Undefined, Any

def header_length(bytearray): pass
def body_length(bytearray): pass
def unquote(s): pass
def quote(c): pass
def header_encode(header_bytes, charset=''): pass
def body_encode(body, maxlinelen=76, eol=Undefined): pass
def decode(encoded, eol=Undefined): pass

body_decode = Undefined(Any)
decodestring = Undefined(Any)

def header_decode(s): pass
