/* Navbar */
function myData() {
    retrun;
  }
  
  function show() {
    document.getElementById('anotherFunction').classList.toggle('Active');
  }
/* End of Navbar */

/* Calendar */
const events = {
  "2024-10-01": { title: "Event 1", description: "Description for Event 1" },
  "2024-10-15": { title: "Event 2", description: "Description for Event 2" },
  "2024-10-23": { title: "Event 3", description: "Description for Event 3" },
};

let currentDate = new Date();

const calendar = document.getElementById("calendar");
const currentMonthDisplay = document.getElementById("currentMonth");
const eventModal = document.getElementById("eventModal");
const eventTitle = document.getElementById("eventTitle");
const eventDescription = document.getElementById("eventDescription");
const closeModal = document.getElementsByClassName("close")[0];

document.getElementById("prevMonth").addEventListener("click", () => {
  currentDate.setMonth(currentDate.getMonth() - 1);
  generateCalendar();
});

document.getElementById("nextMonth").addEventListener("click", () => {
  currentDate.setMonth(currentDate.getMonth() + 1);
  generateCalendar();
});

// Generate the calendar for the current month
function generateCalendar() {
  calendar.innerHTML = ""; // Clear the calendar
  const month = currentDate.getMonth();
  const year = currentDate.getFullYear();

  // Update current month display
  const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  currentMonthDisplay.textContent = `${monthNames[month]} ${year}`;

  // Create header for days of the week
  const daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  daysOfWeek.forEach(day => {
      const dayHeader = document.createElement("div");
      dayHeader.className = "day header";
      dayHeader.textContent = day;
      calendar.appendChild(dayHeader);
  });

  // First day of the month
  const firstDay = new Date(year, month, 1).getDay();
  const lastDate = new Date(year, month + 1, 0).getDate();

  // Fill the calendar with empty spaces before the first day
  for (let i = 0; i < firstDay; i++) {
      const emptyDiv = document.createElement("div");
      calendar.appendChild(emptyDiv);
  }

  // Fill the calendar with days
  for (let day = 1; day <= lastDate; day++) {
      const dayDiv = document.createElement("div");
      dayDiv.className = "day";
      dayDiv.textContent = day;
      const dateString = `${year}-${(month + 1).toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
      
      dayDiv.addEventListener("click", () => showEvent(dateString, month, year));
      calendar.appendChild(dayDiv);
  }
}

// Show event details in the modal
function showEvent(dateString, month, year) {
  const event = events[dateString];
  const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  const currentMonth = monthNames[month];

  if (event) {
      eventTitle.textContent = `${event.title} (${currentMonth} ${year})`;
      eventDescription.textContent = event.description;
      eventModal.style.display = "block";
  } else {
      alert("No events found for this date.");
  }
}

// Close the modal
closeModal.onclick = function() {
  eventModal.style.display = "none";
};

window.onclick = function(event) {
  if (event.target === eventModal) {
      eventModal.style.display = "none";
  }
};

// Initialize calendar
generateCalendar();

/* End of Weekly Schedule */
