// ======================================================
// INTELLIGENCE DASHBOARD
// Part 1
// ======================================================

let dashboardData = {};
let expenseChart = null;
let incomeChart = null;
let trendChart = null;

document.addEventListener("DOMContentLoaded", () => {

    loadDashboardData();

});


// ======================================================
// LOAD JSON
// ======================================================

function loadDashboardData(){

    const dataElement = document.getElementById("dashboard-data");

    if(!dataElement){

        console.error("dashboard-data JSON not found.");

        return;

    }

    try{

        dashboardData = JSON.parse(dataElement.textContent);

        console.log("Dashboard Data");

        console.log(dashboardData);

    }

    catch(error){

        console.error("JSON Error :",error);

        return;

    }

    initialiseDashboard();

}



// ======================================================
// INITIALISE
// ======================================================

function initialiseDashboard(){

    animateHealthScore();

    animateSummaryCards();

    createExpenseChart();

    createIncomeChart();

    createTrendChart();

}



// ======================================================
// HEALTH SCORE
// ======================================================

function animateHealthScore(){

    const element=document.querySelector(".health-score-card h2");

    if(!element) return;

    let score=parseInt(dashboardData.healthScore)||0;

    let count=0;

    const timer=setInterval(()=>{

        count++;

        element.innerHTML=count;

        if(count>=score){

            clearInterval(timer);

        }

    },20);

}



// ======================================================
// SUMMARY COUNTER
// ======================================================

function animateSummaryCards(){

    document.querySelectorAll(".summary-card h3").forEach(card=>{

        const number=parseFloat(

            card.innerText

            .replace("₹","")

            .replace(/,/g,"")

        );

        if(isNaN(number)) return;

        let current=0;

        const increment=number/60;

        card.innerHTML="₹0";

        const timer=setInterval(()=>{

            current+=increment;

            if(current>=number){

                current=number;

                clearInterval(timer);

            }

            card.innerHTML="₹"+Math.round(current).toLocaleString();

        },15);

    });

}



// ======================================================
// COMMON CHART OPTIONS
// ======================================================

function chartOptions(){

    return{

        responsive:true,

        maintainAspectRatio:false,

        plugins:{

            legend:{

                position:"bottom"

            }

        }

    };

}

// ======================================================
// EXPENSE CATEGORY PIE CHART
// ======================================================

function createExpenseChart(){

    const canvas=document.getElementById("expenseCategoryChart");

    if(!canvas){

        console.log("Expense chart canvas not found.");

        return;

    }

    const categories=dashboardData.categories || [];

    if(categories.length===0){

        canvas.parentElement.innerHTML=
        "<div style='padding:40px;text-align:center;'>No Expense Data Available</div>";

        return;

    }

    const labels=[];
    const values=[];

    categories.forEach(item=>{

        labels.push(item.category);
        values.push(Number(item.amount));

    });

    if(expenseChart){

        expenseChart.destroy();

    }

    expenseChart=new Chart(canvas,{

        type:"pie",

        data:{

            labels:labels,

            datasets:[{

                data:values,

                backgroundColor:[

                    "#4f46e5",
                    "#3b82f6",
                    "#10b981",
                    "#f59e0b",
                    "#ef4444",
                    "#8b5cf6",
                    "#06b6d4",
                    "#14b8a6",
                    "#f97316",
                    "#6366f1"

                ],

                borderWidth:2,

                borderColor:"#ffffff"

            }]

        },

        options:chartOptions()

    });

}



// ======================================================
// INCOME VS EXPENSE BAR CHART
// ======================================================

function createIncomeChart(){

    const canvas=document.getElementById("incomeExpenseChart");

    if(!canvas){

        console.log("Income chart canvas not found.");

        return;

    }

    if(incomeChart){

        incomeChart.destroy();

    }

    const income=Number(dashboardData.income)||0;

    const expense=Number(dashboardData.expense)||0;

    const savings=income-expense;

    incomeChart=new Chart(canvas,{

        type:"bar",

        data:{

            labels:[

                "Income",

                "Expense",

                "Savings"

            ],

            datasets:[{

                label:"Amount",

                data:[

                    income,

                    expense,

                    savings

                ],

                backgroundColor:[

                    "#10b981",

                    "#ef4444",

                    "#3b82f6"

                ],

                borderRadius:10

            }]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            plugins:{

                legend:{

                    display:false

                }

            },

            scales:{

                y:{

                    beginAtZero:true

                }

            }

        }

    });

}

// ======================================================
// MONTHLY EXPENSE TREND CHART
// ======================================================

function createTrendChart(){

    const canvas = document.getElementById("monthlyTrendChart");

    if(!canvas){

        console.log("Monthly Trend canvas not found.");

        return;

    }

    const trend = dashboardData.monthlyTrend || [];

    if(trend.length === 0){

        canvas.parentElement.innerHTML =
        "<div style='padding:40px;text-align:center;'>No Monthly Expense Data Available</div>";

        return;

    }

    const labels = [];
    const values = [];

    trend.forEach(item=>{

        labels.push(item.month);
        values.push(Number(item.expense));

    });

    if(trendChart){

        trendChart.destroy();

    }

    trendChart = new Chart(canvas,{

        type:"line",

        data:{

            labels:labels,

            datasets:[{

                label:"Monthly Expense",

                data:values,

                fill:true,

                tension:0.35,

                borderColor:"#4f46e5",

                backgroundColor:"rgba(79,70,229,0.15)",

                borderWidth:3,

                pointRadius:5,

                pointHoverRadius:7

            }]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            plugins:{

                legend:{

                    display:false

                }

            },

            scales:{

                y:{

                    beginAtZero:true

                }

            }

        }

    });

}



// ======================================================
// CARD ANIMATION
// ======================================================

function initialiseAnimations(){

    const cards=document.querySelectorAll(

        ".dashboard-card,.summary-card"

    );

    cards.forEach((card,index)=>{

        card.style.opacity="0";

        card.style.transform="translateY(25px)";

        card.style.transition="all .6s ease";

        setTimeout(()=>{

            card.style.opacity="1";

            card.style.transform="translateY(0px)";

        },index*80);

    });

}



// ======================================================
// HOVER EFFECT
// ======================================================

function initialiseHover(){

    document.querySelectorAll(".dashboard-card").forEach(card=>{

        card.addEventListener("mouseenter",()=>{

            card.style.transform="translateY(-5px)";

        });

        card.addEventListener("mouseleave",()=>{

            card.style.transform="translateY(0px)";

        });

    });

}



// ======================================================
// DARK MODE SUPPORT
// ======================================================

function applyChartTheme(){

    if(typeof Chart==="undefined") return;

    const dark=document.body.classList.contains("dark-mode");

    if(dark){

        Chart.defaults.color="#e5e7eb";
        Chart.defaults.borderColor="#374151";

    }else{

        Chart.defaults.color="#374151";
        Chart.defaults.borderColor="#d1d5db";

    }

}



// ======================================================
// WINDOW RESIZE
// ======================================================

window.addEventListener("resize",()=>{

    if(expenseChart){

        expenseChart.resize();

    }

    if(incomeChart){

        incomeChart.resize();

    }

    if(trendChart){

        trendChart.resize();

    }

});



// ======================================================
// FINAL INITIALIZATION
// ======================================================

window.addEventListener("load",()=>{

    applyChartTheme();

    initialiseAnimations();

    initialiseHover();

    console.log("Intelligence Dashboard Loaded Successfully");

});

