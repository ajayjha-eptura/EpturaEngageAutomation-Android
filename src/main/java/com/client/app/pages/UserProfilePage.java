package com.client.app.pages;

import appium.webdriver.extensions.DriverFactory;
import appium.webdriver.extensions.Utility;
import org.openqa.selenium.By;

public class UserProfilePage extends DriverFactory {

	// Locators
	private final By selectUserProfile_xpath = By.xpath("//android.widget.LinearLayout[@content-desc=\"Profile\"]/android.widget.ImageView");
	private final By defaultLocationField_id = By.id("com.condecosoftware.condeco:id/locationDefault");
	private final By defaultLocation_xpath = By.xpath("//android.widget.TextView[@selected='true']");
	private final By locationCloseButton_id = By.id("com.condecosoftware.condeco:id/closeBtn");
	private final By defaultFloor_id = By.id("com.condecosoftware.condeco:id/floorDefault");
	private final By overlayLocationName_id = By.id("com.condecosoftware.condeco:id/subHeader");
	private final By floorCloseButton_id = By.id("com.condecosoftware.condeco:id/closeBtn");
	//private final By backButton_classname = By.className("android.widget.ImageButton");
	private final By defaultCountryField_id = By.id("com.condecosoftware.condeco:id/textCountry");
	private final By topCountryName_id = By.id("android:id/text1");
	private final By saveButton_id = By.id("com.condecosoftware.condeco:id/save");
	private final By logoutButton_id = By.id("com.condecosoftware.condeco:id/logout");
	private final By logoutPopupMsg_id = By.id("com.condecosoftware.condeco:id/core_dlg_message");
	private final By logoutCancelButton_id = By.id("com.condecosoftware.condeco:id/core_dlg_negative_button");
	private final By closeButton_id = By.id("com.condecosoftware.condeco:id/closeBtn");
	private final By defaultCountry_xpath = By.xpath("//android.widget.TextView[@selected='true']");
	private final By defaultFloorSelected_xpath = By.xpath("//android.widget.TextView[@selected='true']");
	private final By defaultGroup_id = By.id("com.condecosoftware.condeco:id/groupDefault");
	private final By defaultGroupSelected_xpath = By.xpath("//android.widget.TextView[@selected='true']");
	private final By newBookingTab_xpath = By.xpath("//android.widget.LinearLayout[@index='2']");
	private final By bookMeetingSpace_id = By.id("com.condecosoftware.condeco:id/viewBookMeetingSpace");
	private final By continueBtnOnNewBooking_id = By.id("com.condecosoftware.condeco:id/button");
	private final By floorField_id = By.id("com.condecosoftware.condeco:id/textFloor");

	// Variables to store state
	private String defaultCountry;
	private String topCountryValue;
	private String defaultLocation;
	private String defaultGroup;

	//Verify the building the user has currently selected is shown at the top of the overlay
	public void selectUserProfile() {
		try {
			System.out.println("Selecting user profile...");
			Utility.waitForElementUntilPresent(selectUserProfile_xpath, 10);
			Utility.clickElement(selectUserProfile_xpath, 10);
			System.out.println("✅ User profile selected");
		} catch (Exception e) {
			System.out.println("❌ Error selecting user profile: " + e.getMessage());
			throw new RuntimeException("Failed to select user profile", e);
		}
	}

	public String selectDefaultLocation() {
		try {
			System.out.println("Selecting default location...");
			Utility.waitForElementUntilPresent(defaultLocationField_id, 10);
			Utility.clickElement(defaultLocationField_id, 10);
			Thread.sleep(1000);
			defaultLocation = Utility.getTextFromid(defaultLocation_xpath, 10);
			System.out.println("✅ Default location: " + defaultLocation);
			Utility.clickElement(locationCloseButton_id, 10);
			return defaultLocation;
		} catch (Exception e) {
			System.out.println("❌ Error selecting default location: " + e.getMessage());
			throw new RuntimeException("Failed to select default location", e);
		}
	}

	public void selectFloorOption() {
		try {
			System.out.println("Selecting floor option...");
			Utility.clickElement(defaultFloor_id, 10);
			Thread.sleep(1000);
			String actualLocation = Utility.getTextFromid(overlayLocationName_id, 10);
			System.out.println("Overlay location name: " + actualLocation);
			Utility.clickElement(floorCloseButton_id, 10);
			
			// Verify and print location matching
			System.out.println("Verifying location match...");
			System.out.println("Default Location: " + defaultLocation);
			System.out.println("Actual Location: " + actualLocation);
			if (!defaultLocation.equals(actualLocation)) {
				throw new AssertionError("Location names do not match: expected [" + defaultLocation + "] but was [" + actualLocation + "]");
			}
			System.out.println("✅ Location names matched successfully: " + defaultLocation + " == " + actualLocation);
			System.out.println("✅ Building name verified at the top of floor overlay");
		} catch (Exception e) {
			System.out.println("❌ Error selecting floor option: " + e.getMessage());
			throw new RuntimeException("Failed to select floor option", e);
		}
	}

	//Verify the Save button on Default setting screen
	public String selectTopCountry() {
		try {
			System.out.println("Selecting top country...");
			Utility.waitForElementUntilPresent(defaultCountryField_id, 10);
			Utility.clickElement(defaultCountryField_id, 10);
			Thread.sleep(1000);
			topCountryValue = Utility.getTextFromid(topCountryName_id, 10);
			System.out.println("Top country value: " + topCountryValue);
			Utility.clickElement(topCountryName_id, 10);
			return topCountryValue;
		} catch (Exception e) {
			System.out.println("❌ Error selecting top country: " + e.getMessage());
			throw new RuntimeException("Failed to select top country", e);
		}
	}

	public void tapOnSave() {
		try {
			System.out.println("Tapping on Save button...");
			Utility.clickElement(saveButton_id, 10);
			Thread.sleep(2000);
			System.out.println("✅ Save button clicked");
		} catch (Exception e) {
			System.out.println("❌ Error tapping save button: " + e.getMessage());
			throw new RuntimeException("Failed to tap save button", e);
		}
	}

	public void validateSavedValue() {
		try {
			System.out.println("Validating saved value...");
			Utility.waitForElementUntilPresent(selectUserProfile_xpath, 10);
			Utility.clickElement(selectUserProfile_xpath, 10);
			Thread.sleep(1000);
			String updatedValue = Utility.getTextFromid(defaultCountryField_id, 10);
			System.out.println("Updated value: " + updatedValue);
			if (!topCountryValue.equals(updatedValue)) {
				throw new AssertionError("Saved value does not match expected value: expected [" + topCountryValue + "] but was [" + updatedValue + "]");
			}
			System.out.println("✅ Changed value successfully updated");
		} catch (Exception e) {
			System.out.println("❌ Error validating saved value: " + e.getMessage());
			throw new RuntimeException("Failed to validate saved value", e);
		}
	}

	// Verify the pop up shown on log out button on Default setting screen
	public void selectLogoutButton() {
		try {
			System.out.println("Selecting logout button...");
			Utility.waitForElementUntilPresent(logoutButton_id, 10);
			Utility.clickElement(logoutButton_id, 10);
			Thread.sleep(1000);
			System.out.println("✅ Logout button clicked");
		} catch (Exception e) {
			System.out.println("❌ Error selecting logout button: " + e.getMessage());
			throw new RuntimeException("Failed to select logout button", e);
		}
	}

	public void verifyLogoutPopupShown(String expectedLogoutPopupMsg) {
		try {
			System.out.println("Verifying logout popup message...");
			String actualMsg = Utility.getTextFromid(logoutPopupMsg_id, 10);
			System.out.println("Popup message: " + actualMsg);
			Utility.clickElement(logoutCancelButton_id, 10);
			Thread.sleep(1000);
			if (!expectedLogoutPopupMsg.equals(actualMsg)) {
				throw new AssertionError("Logout popup message does not match: expected [" + expectedLogoutPopupMsg + "] but was [" + actualMsg + "]");
			}
			System.out.println("✅ Logout popup verified successfully");
		} catch (Exception e) {
			System.out.println("❌ Error verifying logout popup: " + e.getMessage());
			throw new RuntimeException("Failed to verify logout popup", e);
		}
	}

	//Verify if the user chooses to close the overlay without making a selection
	public String selectDefaultCountry() {
		try {
			System.out.println("Selecting default country...");
			Utility.waitForElementUntilPresent(defaultCountryField_id, 10);
			Utility.clickElement(defaultCountryField_id, 10);
			Thread.sleep(1000);
			defaultCountry = Utility.getTextFromid(defaultCountry_xpath, 10);
			System.out.println("Default country: " + defaultCountry);
			return defaultCountry;
		} catch (Exception e) {
			System.out.println("❌ Error selecting default country: " + e.getMessage());
			throw new RuntimeException("Failed to select default country", e);
		}
	}

	public void selectCloseButton() {
		try {
			System.out.println("Clicking close button...");
			Utility.clickElement(closeButton_id, 10);
			Thread.sleep(1000);
			System.out.println("✅ Close button clicked");
		} catch (Exception e) {
			System.out.println("❌ Error clicking close button: " + e.getMessage());
			throw new RuntimeException("Failed to click close button", e);
		}
	}

	public void verifyCountryNameNotChanged() {
		try {
			System.out.println("Verifying country name not changed...");
			Utility.clickElement(defaultCountryField_id, 10);
			Thread.sleep(1000);
			String latestCountry = Utility.getTextFromid(defaultCountry_xpath, 10);
			System.out.println("Latest country: " + latestCountry);
			Utility.clickElement(closeButton_id, 10);
			if (!defaultCountry.equals(latestCountry)) {
				throw new AssertionError("Country selection changed unexpectedly: expected [" + defaultCountry + "] but was [" + latestCountry + "]");
			}
			System.out.println("✅ Previously selected country not changed");
		} catch (Exception e) {
			System.out.println("❌ Error verifying country name: " + e.getMessage());
			throw new RuntimeException("Failed to verify country name", e);
		}
	}

	//Verify when the user presses the 'Floor' button, the Floor selection overlay appears
	public void tapOnFloorOption() {
		try {
			System.out.println("Tapping on floor option...");
			Utility.waitForElementUntilPresent(defaultFloor_id, 10);
			Utility.clickElement(defaultFloor_id, 10);
			Thread.sleep(1000);
			System.out.println("✅ Floor option tapped");
		} catch (Exception e) {
			System.out.println("❌ Error tapping floor option: " + e.getMessage());
			throw new RuntimeException("Failed to tap floor option", e);
		}
	}

	public void verifyFloorSelectionOverlay() {
		try {
			System.out.println("Verifying floor selection overlay...");
			boolean floorSelection = Utility.isElementPresent(defaultFloorSelected_xpath, 10);
			if (floorSelection) {
				System.out.println("✅ Floor selection overlay appears");
				Utility.clickElement(closeButton_id, 10);
			} else {
				throw new AssertionError("Floor selection overlay not found");
			}
		} catch (Exception e) {
			System.out.println("❌ Error verifying floor selection overlay: " + e.getMessage());
			throw new RuntimeException("Failed to verify floor selection overlay", e);
		}
	}

	//Verify when the user presses the 'Group' button
	public void tapOnGroupOption() {
		try {
			System.out.println("Tapping on group option...");
			Utility.waitForElementUntilPresent(defaultGroup_id, 10);
			Utility.clickElement(defaultGroup_id, 10);
			Thread.sleep(1000);
			System.out.println("✅ Group option tapped");
		} catch (Exception e) {
			System.out.println("❌ Error tapping group option: " + e.getMessage());
			throw new RuntimeException("Failed to tap group option", e);
		}
	}

	public void verifyGroupSelectionOverlay() {
		try {
			System.out.println("Verifying group selection overlay...");
			boolean groupSelection = Utility.isElementPresent(defaultGroupSelected_xpath, 10);
			if (groupSelection) {
				System.out.println("✅ Group selection overlay appears");
				Utility.clickElement(closeButton_id, 10);
			} else {
				throw new AssertionError("Group selection overlay not found");
			}
		} catch (Exception e) {
			System.out.println("❌ Error verifying group selection overlay: " + e.getMessage());
			throw new RuntimeException("Failed to verify group selection overlay", e);
		}
	}

	//  Verify that selected a WSType exists on the user default floor
	public void navigateToNewBooking() {
		try {
			System.out.println("Navigating to new booking...");
			Utility.waitForElementUntilPresent(newBookingTab_xpath, 10);
			Utility.clickElement(newBookingTab_xpath, 10);
			Thread.sleep(2000);
			System.out.println("✅ Navigated to New Booking Page");
		} catch (Exception e) {
			System.out.println("❌ Error navigating to new booking: " + e.getMessage());
			throw new RuntimeException("Failed to navigate to new booking", e);
		}
	}

	public void expandBookMeetingSpaceSection() {
		try {
			System.out.println("Expanding book meeting space section...");
			Utility.waitForElementUntilPresent(bookMeetingSpace_id, 10);
			Utility.clickElement(bookMeetingSpace_id, 10);
			Thread.sleep(1000);
			System.out.println("✅ Book meeting space section expanded");
		} catch (Exception e) {
			System.out.println("❌ Error expanding book meeting space: " + e.getMessage());
			throw new RuntimeException("Failed to expand book meeting space section", e);
		}
	}

	public void pressContinue() {
		try {
			System.out.println("Pressing continue button...");
			Utility.clickElement(continueBtnOnNewBooking_id, 10);
			Thread.sleep(2000);
			System.out.println("✅ Continue button pressed");
		} catch (Exception e) {
			System.out.println("❌ Error pressing continue: " + e.getMessage());
			throw new RuntimeException("Failed to press continue button", e);
		}
	}

	public boolean verifyFloorOnWSType(String expectedFloor) {
		try {
			System.out.println("Verifying floor on WSType...");
			System.out.println("Expected floor: " + expectedFloor);
			Utility.waitForElementUntilPresent(floorField_id, 10);
			String actualFloorValue = Utility.getTextFromid(floorField_id, 10);
			System.out.println("Actual floor: " + actualFloorValue);
			
			if (actualFloorValue.equals(expectedFloor)) {
				System.out.println("✅ Floor value matches expected value");
				return true;
			} else {
				System.out.println("❌ Floor value does not match");
				return false;
			}
		} catch (Exception e) {
			System.out.println("❌ Error verifying floor on WSType: " + e.getMessage());
			throw new RuntimeException("Failed to verify floor on WSType", e);
		}
	}

	//  Verify the current selection of floor is highlighted
	public void verifyFloorHighlighted() {
		try {
			System.out.println("Verifying floor is highlighted...");
			String selectedFloor = Utility.getTextFromid(defaultFloorSelected_xpath, 10);
			System.out.println("Selected Floor is: " + selectedFloor);
			
			boolean floorFound = false;
			for (int i = 0; i <= 20; i++) {
				try {
					By floorListItem = By.xpath("//android.widget.LinearLayout[@clickable='true'][@index=" + i + "]//child::*");
					if (Utility.isElementPresent(floorListItem, 2)) {
						String floorList = Utility.getTextFromid(floorListItem, 2);
						System.out.println("Floor Name is: " + floorList);
						
						if (selectedFloor.equals(floorList)) {
							System.out.println("✅ Selected floor found in the list and is highlighted");
							floorFound = true;
							break;
						}
					}
				} catch (Exception e) {
					// Continue to next iteration
					continue;
				}
			}
			
			Utility.clickElement(closeButton_id, 10);
			
			if (!floorFound) {
				throw new AssertionError("Selected floor not found in the list");
			}
		} catch (Exception e) {
			System.out.println("❌ Error verifying floor highlighted: " + e.getMessage());
			throw new RuntimeException("Failed to verify floor highlighted", e);
		}
	}

	//  Verify the current selection of Group is highlighted
	public void verifyGroupHighlighted() {
		try {
			System.out.println("Verifying group is highlighted...");
			String selectedGroup = Utility.getTextFromid(defaultGroupSelected_xpath, 10);
			System.out.println("Selected Group is: " + selectedGroup);
			
			boolean groupFound = false;
			for (int i = 0; i <= 20; i++) {
				try {
					By groupListItem = By.xpath("//android.widget.LinearLayout[@clickable='true'][@index=" + i + "]//child::*");
					if (Utility.isElementPresent(groupListItem, 2)) {
						String groupList = Utility.getTextFromid(groupListItem, 2);
						System.out.println("Group Name is: " + groupList);
						
						if (selectedGroup.equals(groupList)) {
							System.out.println("✅ Selected group found in the list and is highlighted");
							groupFound = true;
							break;
						}
					}
				} catch (Exception e) {
					// Continue to next iteration
					continue;
				}
			}
			
			Utility.clickElement(closeButton_id, 10);
			
			
			if (!groupFound) {
				throw new AssertionError("Selected group not found in the list");
			}
		} catch (Exception e) {
			System.out.println("❌ Error verifying group highlighted: " + e.getMessage());
			throw new RuntimeException("Failed to verify group highlighted", e);
		}
	}

	//  Verify if the user chooses to close the overlay without making a selection
	public String selectDefaultGroup() {
		try {
			System.out.println("Selecting default group...");
			Utility.waitForElementUntilPresent(defaultGroup_id, 10);
			Utility.clickElement(defaultGroup_id, 10);
			Thread.sleep(1000);
			defaultGroup = Utility.getTextFromid(defaultGroupSelected_xpath, 10);
			System.out.println("Default group: " + defaultGroup);
			return defaultGroup;
		} catch (Exception e) {
			System.out.println("❌ Error selecting default group: " + e.getMessage());
			throw new RuntimeException("Failed to select default group", e);
		}
	}

	public void verifyGroupNameNotChanged() {
		try {
			System.out.println("Verifying group name not changed...");
			Utility.clickElement(defaultGroup_id, 10);
			Thread.sleep(1000);
			String latestGroup = Utility.getTextFromid(defaultGroupSelected_xpath, 10);
			System.out.println("Latest group: " + latestGroup);
			Utility.clickElement(closeButton_id, 10);
			if (!defaultGroup.equals(latestGroup)) {
				throw new AssertionError("Group selection changed unexpectedly: expected [" + defaultGroup + "] but was [" + latestGroup + "]");
			}
			System.out.println("✅ Previously selected group not changed");
		} catch (Exception e) {
			System.out.println("❌ Error verifying group name: " + e.getMessage());
			throw new RuntimeException("Failed to verify group name", e);
		}
	}
}