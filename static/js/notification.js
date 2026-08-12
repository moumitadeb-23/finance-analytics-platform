/*=====================================================
 FINANCE ANALYTICS PLATFORM
 Notification Center
 Part 1
=====================================================*/

document.addEventListener("DOMContentLoaded", function () {

    initializeNotificationDashboard();

});

/*=====================================================
 INITIALIZATION
=====================================================*/

function initializeNotificationDashboard() {

    loadDashboardData();

    initializeGaugeChart();

    initializeSearch();

    animateSummaryCards();

}

/*=====================================================
 LOAD JSON DATA
=====================================================*/

let dashboardData = {};

function loadDashboardData() {

    const jsonElement = document.getElementById("notification-data");

    if (!jsonElement) {

        console.error("Notification JSON not found");

        return;

    }

    try {

        dashboardData = JSON.parse(jsonElement.textContent);

    }

    catch (error) {

        console.error("Invalid notification JSON", error);

    }

}

/*=====================================================
 GAUGE CHART
=====================================================*/

let gaugeChart = null;

function initializeGaugeChart() {

    const canvas = document.getElementById("notificationGauge");

    if (!canvas) return;

    const ctx = canvas.getContext("2d");

    let total = dashboardData.totalNotifications || 0;

    let value = total;

    if (value > 100) {

        value = 100;

    }

    gaugeChart = new Chart(ctx, {

        type: "doughnut",

        data: {

            datasets: [

                {

                    data: [

                        value,

                        100 - value

                    ],

                    backgroundColor: [

                        "#4f46e5",

                        "#e5e7eb"

                    ],

                    borderWidth: 0,

                    circumference: 180,

                    rotation: 270,

                    cutout: "75%"

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: false

                },

                tooltip: {

                    enabled: false

                }

            }

        },

        plugins: [

            {

                id: "centerText",

                afterDraw(chart) {

                    const {

                        width,

                        height,

                        ctx

                    } = chart;

                    ctx.restore();

                    ctx.font = "bold 26px Poppins";

                    ctx.fillStyle = "#111827";

                    ctx.textAlign = "center";

                    ctx.fillText(

                        total,

                        width / 2,

                        height / 1.3

                    );

                    ctx.font = "14px Poppins";

                    ctx.fillStyle = "#6b7280";

                    ctx.fillText(

                        "Notifications",

                        width / 2,

                        height / 1.3 + 22

                    );

                    ctx.save();

                }

            }

        ]

    });

}

/*=====================================================
 SEARCH TABLE
=====================================================*/

function initializeSearch() {

    const searchBox = document.getElementById("searchNotification");

    if (!searchBox) return;

    searchBox.addEventListener("keyup", function () {

        const keyword = this.value.toLowerCase();

        const rows = document.querySelectorAll("#notificationTable tbody tr");

        rows.forEach(function (row) {

            const text = row.innerText.toLowerCase();

            if (text.includes(keyword)) {

                row.style.display = "";

            }

            else {

                row.style.display = "none";

            }

        });

    });

}

/*=====================================================
 KPI ANIMATION
=====================================================*/

function animateSummaryCards() {

    const numbers = document.querySelectorAll(".summary-card h2");

    numbers.forEach(function (number) {

        let target = parseInt(number.innerText);

        if (isNaN(target)) return;

        let current = 0;

        const increment = Math.ceil(target / 40);

        number.innerText = "0";

        const counter = setInterval(function () {

            current += increment;

            if (current >= target) {

                current = target;

                clearInterval(counter);

            }

            number.innerText = current;

        }, 25);

    });

}

/*=====================================================
 PART 2
 Dashboard Animation & Notification Utilities
=====================================================*/

/*=====================================================
 CARD HOVER EFFECTS
=====================================================*/

function initializeCardAnimations() {

    const cards = document.querySelectorAll(
        ".notification-card,.summary-card,.panel,.insight-card,.bill-item,.stat-box"
    );

    cards.forEach(function(card){

        card.addEventListener("mouseenter",function(){

            this.style.transition="all .3s ease";
            this.style.transform="translateY(-5px)";

        });

        card.addEventListener("mouseleave",function(){

            this.style.transform="translateY(0px)";

        });

    });

}

/*=====================================================
 UPDATE UNREAD BADGES
=====================================================*/

function updateUnreadCount(){

    const unreadCards=document.querySelectorAll(".notification-card.unread");

    const unreadBadges=document.querySelectorAll(".badge.unread");

    const total=unreadCards.length;

    unreadBadges.forEach(function(badge){

        badge.innerHTML="Unread";

    });

    console.log("Unread Notifications :",total);

}

/*=====================================================
 MARK READ ANIMATION
=====================================================*/

function initializeReadButtons(){

    const buttons=document.querySelectorAll(".btn-read");

    buttons.forEach(function(button){

        button.addEventListener("click",function(){

            const card=this.closest(".notification-card");

            if(card){

                card.classList.remove("unread");

                card.style.opacity=".7";

            }

        });

    });

}

/*=====================================================
 DELETE ANIMATION
=====================================================*/

function initializeDeleteButtons(){

    const buttons=document.querySelectorAll(".btn-delete");

    buttons.forEach(function(button){

        button.addEventListener("click",function(e){

            const confirmDelete=confirm(
                "Delete this notification?"
            );

            if(!confirmDelete){

                e.preventDefault();
                return;

            }

            const card=this.closest(".notification-card");

            if(card){

                card.style.transition=".4s";
                card.style.opacity="0";
                card.style.transform="translateX(100px)";

            }

        });

    });

}

/*=====================================================
 SCROLL ANIMATION
=====================================================*/

function initializeScrollAnimation(){

    const observer=new IntersectionObserver(function(entries){

        entries.forEach(function(entry){

            if(entry.isIntersecting){

                entry.target.style.opacity="1";

                entry.target.style.transform="translateY(0px)";

            }

        });

    },{

        threshold:.15

    });

    document.querySelectorAll(".notification-card,.panel").forEach(function(el){

        el.style.opacity="0";

        el.style.transform="translateY(25px)";

        observer.observe(el);

    });

}

/*=====================================================
 PANEL FADE
=====================================================*/

function animatePanels(){

    const panels=document.querySelectorAll(".panel");

    panels.forEach(function(panel,index){

        panel.style.animationDelay=(index*.15)+"s";

    });

}

/*=====================================================
 AUTO REFRESH CLOCK
=====================================================*/

function updateCurrentTime(){

    const now=new Date();

    console.log(

        "Notification Center Loaded :",

        now.toLocaleTimeString()

    );

}

/*=====================================================
 INITIALIZE PART 2
=====================================================*/

document.addEventListener("DOMContentLoaded",function(){

    initializeCardAnimations();

    initializeReadButtons();

    initializeDeleteButtons();

    initializeScrollAnimation();

    animatePanels();

    updateUnreadCount();

    updateCurrentTime();

});

/*=====================================================
 FINANCE ANALYTICS PLATFORM
 Notification Center
 Part 3
======================================================*/

/*=====================================================
 AUTO REFRESH (Optional)
======================================================*/

const AUTO_REFRESH_INTERVAL = 300000; // 5 Minutes

function startAutoRefresh(){

    setInterval(function(){

        console.log("Refreshing notification dashboard...");

        location.reload();

    },AUTO_REFRESH_INTERVAL);

}

/*=====================================================
 TOAST MESSAGE
======================================================*/

function showToast(message,type="success"){

    const toast=document.createElement("div");

    toast.className="notification-toast";

    toast.innerHTML=`
        <i class="fas fa-check-circle"></i>
        <span>${message}</span>
    `;

    if(type==="error"){

        toast.style.background="#ef4444";

    }

    document.body.appendChild(toast);

    setTimeout(function(){

        toast.classList.add("show");

    },100);

    setTimeout(function(){

        toast.classList.remove("show");

        setTimeout(function(){

            toast.remove();

        },400);

    },3000);

}

/*=====================================================
 BUTTON FEEDBACK
======================================================*/

function initializeButtons(){

    document.querySelectorAll(".btn-read").forEach(function(btn){

        btn.addEventListener("click",function(){

            showToast("Notification marked as read");

        });

    });

    document.querySelectorAll(".btn-delete").forEach(function(btn){

        btn.addEventListener("click",function(){

            showToast("Notification deleted","error");

        });

    });

}

/*=====================================================
 TABLE ROW HIGHLIGHT
======================================================*/

function highlightRows(){

    const rows=document.querySelectorAll("#notificationTable tbody tr");

    rows.forEach(function(row){

        row.addEventListener("mouseenter",function(){

            this.style.background="#eef4ff";

        });

        row.addEventListener("mouseleave",function(){

            this.style.background="";

        });

    });

}

/*=====================================================
 LIVE CLOCK
======================================================*/

function updateClock(){

    const now=new Date();

    console.log(

        "Dashboard Time : ",

        now.toLocaleString()

    );

}

/*=====================================================
 INITIALIZE
======================================================*/

document.addEventListener("DOMContentLoaded",function(){

    initializeButtons();

    highlightRows();

    updateClock();

    // Uncomment if you want automatic refresh
    // startAutoRefresh();

});

