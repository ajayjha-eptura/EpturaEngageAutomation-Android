#Author: Ajay.jha@eptura.com

Feature: US #: Verify login flow for Eptura Engage  mobile Application

Scenario:CUMA-C98620 Verify that user is not able to login using wrong credentials.
 Given User is on Login page
 When User attempts Forms Login with wrong password as "incorrectpassword"
 Then Verify authentication failed message


Scenario:CUMA-C226538 Perform Login with valid credentials
 Given User is on Login page
 When User performs Forms Login
 Then User successfully logged-in