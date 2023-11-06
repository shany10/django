document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');
  const button = document.getElementById('submit');

  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar: {
      right: 'prev today next',
      center: 'title',
      left: 'dayGridMonth,timeGridWeek,timeGridDay,list'
    },
  });

  button.onclick = function() {
    var student = document.getElementById('student').value;
    var instructeur = document.getElementById('instructor').value;
    var dateStr = document.getElementById('startDate').value;
    var date = new Date(dateStr); // will be in local time

    if (!isNaN(date.valueOf())) { // valid?
      calendar.addEvent({
        title: student,
        start: date,
        instructeur: instructeur,
      });
    } 
  }
  calendar.render();
});