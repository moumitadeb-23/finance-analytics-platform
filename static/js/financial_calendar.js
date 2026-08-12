document.addEventListener("DOMContentLoaded", function () {

    const calendarEl = document.getElementById("calendar");

    const calendar = new FullCalendar.Calendar(calendarEl, {

        initialView: "dayGridMonth",

        height: 700,

        headerToolbar: {

            left: "prev,next today",

            center: "title",

            right: "dayGridMonth,timeGridWeek,timeGridDay"

        },

        events: "/api/calendar-events",

        eventClick:function(info){

        Swal.fire({

            title:info.event.title,

            html:`

            <b>Date</b><br>

            ${info.event.start.toLocaleDateString()}

            `,

            icon:"info",

            confirmButtonText:"Close"

        });

    }

    });

    calendar.render();

});

async function loadSummary() {

    try {

        const response = await fetch("/api/calendar-summary");

        const data = await response.json();

        console.log(data);

        document.getElementById("sumIncome").innerHTML =
            "₹" + Number(data.income).toLocaleString();

        document.getElementById("sumExpense").innerHTML =
            "₹" + Number(data.expense).toLocaleString();

        document.getElementById("sumSavings").innerHTML =
            "₹" + Number(data.savings).toLocaleString();

        document.getElementById("sumInvestment").innerHTML =
            "₹" + Number(data.investment).toLocaleString();

        document.getElementById("sumGoals").innerHTML =
            data.goals;

        document.getElementById("budgetText").innerHTML =
            data.budget_percent + "%";

        document.getElementById("budgetBar").style.width =
            data.budget_percent + "%";

    }

    catch(error){

        console.log(error);

    }

}

document.addEventListener("DOMContentLoaded", function () {

    loadSummary();

});