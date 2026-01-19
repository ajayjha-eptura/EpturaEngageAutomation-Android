package com.client.app.stepDefs;

import org.testng.Assert;
import com.client.app.pages.UserProfilePage;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.And;

public class UserProfileStepDef {

	private final UserProfilePage userProfilePage = new UserProfilePage();

	//Verify the building the user has currently selected is shown at the top of the overlay
	@Given("User is on user profile page")
	public void user_is_on_profile_page() {
		userProfilePage.selectUserProfile();
	}

	@When("User tap on default location option of personal space")
	public void user_tap_on_default_location_option() {
		userProfilePage.selectDefaultLocation();
	}

	@Then("Building name is displayed at the top of floor overlay")
	public void user_tap_on_floor_option() {
		userProfilePage.selectFloorOption();
	}

	//Verify the Save button on Default setting screen
	@When("User tap on country option of personal space and choose the country")
	public void user_tap_on_country_option() {
		userProfilePage.selectTopCountry();
	}

	@And("User press the save button")
	public void user_press_on_save_button() {
		userProfilePage.tapOnSave();
	}

	@Then("Changed value should get successfully updated")
	public void validate_saved_value() {
		userProfilePage.validateSavedValue();
	}

	//Verify the pop up shown on log out button on Default setting screen
	@When("User tap on the logout button")
	public void user_tap_on_logout_button() {
		userProfilePage.selectLogoutButton();
	}

	@Then("Pop up is shown on tapping logout button {string}")
	public void popup_on_tapping_logout_button(String logoutPopupMsg) {
		userProfilePage.verifyLogoutPopupShown(logoutPopupMsg);
	}

	// Verify if the user chooses to close the overlay without making a selection, 
	// the previously selected country is not changed
	@When("User tap on country option of personal space and choose the default country")
	public void user_tap_on_default_country_option() {
		userProfilePage.selectDefaultCountry();
	}

	@And("User press the close button")
	public void user_tap_on_close_button() {
		userProfilePage.selectCloseButton();
	}

	@Then("Previously selected country should not be changed if no selection is made")
	public void verify_country_name_not_changed() {
		userProfilePage.verifyCountryNameNotChanged();
	}

	//  Verify when the user presses the 'Floor' button, the Floor selection overlay appears
	@When("User tap on floor option")
	public void user_tap_on_floor() {
		userProfilePage.tapOnFloorOption();
	}

	@Then("The floor selection overlay appears")
	public void verify_floor_selection_overlay() {
		userProfilePage.verifyFloorSelectionOverlay();
	}

	//  Verify when the user presses the 'Group' button, the Group selection overlay appears
	@When("User tap on group option")
	public void user_tap_on_group() {
		userProfilePage.tapOnGroupOption();
	}

	@Then("The group selection overlay appears")
	public void verify_group_selection_overlay() {
		userProfilePage.verifyGroupSelectionOverlay();
	}

	// Verify that selected a WSType exists on the user default floor then 
	// the default floor will be shown selected
	@Given("User is navigated to New Booking Page")
	public void user_Navigate_To_NewBooking() {
		userProfilePage.navigateToNewBooking();
	}

	@When("User Tap on Book a Meeting space")
	public void tap_Book_MeetingSpace() {
		userProfilePage.expandBookMeetingSpaceSection();
	}

	@And("Press Continue on New Booking")
	public void press_Contine() {
		userProfilePage.pressContinue();
	}

	@Then("Verify Floor value as {string}")
	public void verify_Floor_Based_On_WSType(String floor) {
		Assert.assertTrue(userProfilePage.verifyFloorOnWSType(floor), 
			"Floor value does not match expected: " + floor);
	}

	//Verify the current selection of floor is highlighted
	@Then("The current selection of floor is highlighted")
	public void verify_floor_highlighted() {
		userProfilePage.verifyFloorHighlighted();
	}

	//Verify the current selection of Group is highlighted
	@Then("The current selection of Group is highlighted")
	public void verify_Group_highlighted() {
		userProfilePage.verifyGroupHighlighted();
	}

	//Verify if the user chooses to close the overlay without making a selection,
	// the previously selected Group is not changed
	@When("User tap on group option of personal space and choose the default country")
	public void user_tap_on_default_group_option() {
		userProfilePage.selectDefaultGroup();
	}

	@Then("Previously selected group should not be changed if no selection is made")
	public void verify_group_name_not_changed() {
		userProfilePage.verifyGroupNameNotChanged();
	}
}
