$(document).ready(function() {
	const selectedAmenities = []; // Initialize an empty array to store checked amenity IDs

	// Listen for changes on checkboxes
	$('input[type="checkbox"]').on('change', function() {
		const amenityId = $(this).data('id');
		const amenityName = $(this).data('name');

		if ($(this).prop('checked')) {
			// Checkbox is checked, add to selected amenities
			selectedAmenities.push(amenityId);
		} else {
			// Checkbox is unchecked, remove from selected amenities
			const index = selectedAmenities.indexOf(amenityId);
			if (index !== -1) {
				selectedAmenities.splice(index, 1);
			}
		}

		// Update the displayed amenities
		$('#selectedAmenities').text('Selected Amenities: ' + selectedAmenities.join(', '));
	});
});