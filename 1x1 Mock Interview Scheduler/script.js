<<<<<<< HEAD
// Sample JSON data for mentors
const data = {
    "mentors": [
        {
            "id": 1,
            "name": "John Doe",
            "availability": ["2024-08-12T09:00:00", "2024-08-12T09:30:00", "2024-08-12T10:00:00"],
            "areasOfInterest": ["FMCG Sales", "Digital Marketing"],
            "preferredByStudents": true
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "availability": ["2024-08-12T11:00:00", "2024-08-12T11:30:00", "2024-08-12T12:00:00"],
            "areasOfInterest": ["Equity Research", "FMCG Sales"],
            "preferredByStudents": false
        }
    ]
};

// Function to populate the mentor dropdown based on the selected area of interest
function populateMentorDropdown() {
    const areaOfInterest = document.getElementById("areaOfInterest").value;
    const mentorDropdown = document.getElementById("mentor");
    mentorDropdown.innerHTML = '<option value="">Any Available Mentor</option>';

    data.mentors.forEach(mentor => {
        if (mentor.areasOfInterest.includes(areaOfInterest)) {
            const option = document.createElement("option");
            option.value = mentor.id;
            option.textContent = mentor.name;
            mentorDropdown.appendChild(option);
        }
    });
}

// Function to calculate and display payment amount based on session duration
function calculatePayment() {
    const duration = parseInt(document.getElementById("duration").value);
    const paymentAmount = duration * 100; // Example: 2000 for 30 mins, etc.
    document.getElementById("payment").value = `₹${paymentAmount}`;
}

// Event listeners
document.getElementById("areaOfInterest").addEventListener("change", populateMentorDropdown);
document.getElementById("duration").addEventListener("change", calculatePayment);

document.getElementById("submit").addEventListener("click", () => {
    const selectedMentor = document.getElementById("mentor").value;
    const selectedTimeSlot = document.getElementById("timeSlot").value;
    const sessionDuration = document.getElementById("duration").value;
    const paymentAmount = document.getElementById("payment").value;

    // Create a booking object
    const booking = {
        mentorId: selectedMentor,
        timeSlot: selectedTimeSlot,
        duration: sessionDuration,
        payment: paymentAmount
    };

    console.log("Booking Details:", booking);
    alert("Your session has been scheduled!");
});
=======
// Sample JSON data for mentors
const data = {
    "mentors": [
        {
            "id": 1,
            "name": "John Doe",
            "availability": ["2024-08-12T09:00:00", "2024-08-12T09:30:00", "2024-08-12T10:00:00"],
            "areasOfInterest": ["FMCG Sales", "Digital Marketing"],
            "preferredByStudents": true
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "availability": ["2024-08-12T11:00:00", "2024-08-12T11:30:00", "2024-08-12T12:00:00"],
            "areasOfInterest": ["Equity Research", "FMCG Sales"],
            "preferredByStudents": false
        }
    ]
};

// Function to populate the mentor dropdown based on the selected area of interest
function populateMentorDropdown() {
    const areaOfInterest = document.getElementById("areaOfInterest").value;
    const mentorDropdown = document.getElementById("mentor");
    mentorDropdown.innerHTML = '<option value="">Any Available Mentor</option>';

    data.mentors.forEach(mentor => {
        if (mentor.areasOfInterest.includes(areaOfInterest)) {
            const option = document.createElement("option");
            option.value = mentor.id;
            option.textContent = mentor.name;
            mentorDropdown.appendChild(option);
        }
    });
}

// Function to calculate and display payment amount based on session duration
function calculatePayment() {
    const duration = parseInt(document.getElementById("duration").value);
    const paymentAmount = duration * 100; // Example: 2000 for 30 mins, etc.
    document.getElementById("payment").value = `₹${paymentAmount}`;
}

// Event listeners
document.getElementById("areaOfInterest").addEventListener("change", populateMentorDropdown);
document.getElementById("duration").addEventListener("change", calculatePayment);

document.getElementById("submit").addEventListener("click", () => {
    const selectedMentor = document.getElementById("mentor").value;
    const selectedTimeSlot = document.getElementById("timeSlot").value;
    const sessionDuration = document.getElementById("duration").value;
    const paymentAmount = document.getElementById("payment").value;

    // Create a booking object
    const booking = {
        mentorId: selectedMentor,
        timeSlot: selectedTimeSlot,
        duration: sessionDuration,
        payment: paymentAmount
    };

    console.log("Booking Details:", booking);
    alert("Your session has been scheduled!");
});
>>>>>>> 5773a0b1000a0d1ae13e3ca65d37d8b85d2926cf
