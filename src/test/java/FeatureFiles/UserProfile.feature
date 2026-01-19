#Author: Ajay.jha@eptura.com
Feature: US #: User Profile

Scenario:CUMA-C255123 Verify the building the user has currently selected is shown at the top of the overlay
 Given User is on user profile page
 When User tap on default location option of personal space
 Then Building name is displayed at the top of floor overlay
 
 Scenario Outline:CUMA-C255126 Verify the pop up shown on log out button on Default setting screen.
  Given User is on user profile page
  When User tap on the logout button
  Then Pop up is shown on tapping logout button "<logoutPopupMsg>"
Examples:
|logoutPopupMsg|
|Are you sure you want to log out?| 
 
Scenario:CUMA-C255127 Verify the Save button on Default setting screen.
 Given User is on user profile page
 When User tap on country option of personal space and choose the country
 And User press the save button
 Then Changed value should get successfully updated


Scenario:CUMA-C255125 Verify if the user chooses to close the overlay without making a selection, the previously selected country is not changed.
  Given User is on user profile page
  When User tap on country option of personal space and choose the default country
  And User press the close button
  Then Previously selected country should not be changed if no selection is made

Scenario:CUMA-C255124 Verify when the user presses the 'Floor' button, the Floor selection overlay appears
  Given User is on user profile page
  When User tap on floor option
  Then The floor selection overlay appears
  
Scenario:CUMA-C255120-Verify when the user presses the Group button, the Group selection overlay appears.
 Given User is on user profile page
 When User tap on group option
 Then The group selection overlay appears

Scenario:CUMA-C255324-Verify the current selection of floor is highlighted.
 Given User is on user profile page
 When User tap on floor option
 Then The current selection of floor is highlighted 
 
 Scenario:CUMA-C255122-Verify the current selection of Group is highlighted.
 Given User is on user profile page
 When User tap on group option
 Then The current selection of Group is highlighted
 


