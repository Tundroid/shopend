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

	// Make an HTTP request to the API endpoint
	fetch('http://0.0.0.0:5001/api/v1/status/')
		.then(response => response.json())
		.then(data => {
			const apiStatusDiv = document.getElementById('api_status');

			if (data.status === 'OK') {
				// Add the class 'available' to the div#api_status
				apiStatusDiv.classList.add('available');
			} else {
				// Remove the class 'available' from the div#api_status
				apiStatusDiv.classList.remove('available');
			}
		})
		.catch(error => {
			console.error('Error fetching API status:', error);
	});

});