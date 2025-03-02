---
# An instance of the Contact widget.
# Documentation: https://hugoblox.com/docs/page-builder/
widget: contact

# This file represents a page section.
headless: true
active: false  # Set to false to remove from site

# Order that this section appears on the page.
weight: 130

title: Contact
subtitle:

content:
  # Contact (edit or remove options as required)
  email: sbonelo.mdluli@gmail.com
  phone:
  address:
    street:
    city: Johannesburg
    region: Gauteng
    postcode:
    country: South Africa
    country_code: ZA
  coordinates:
    latitude:
    longitude:
  directions:
  office_hours:
  appointment_url:
  #contact_links:

  # Automatically link email and phone or display as text?
  autolink: true

  # Email form provider
  form:
    provider: netlify
    formspree:
      id:
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: false

design:
  columns: '2'
---