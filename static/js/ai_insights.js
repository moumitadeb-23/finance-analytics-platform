/*=====================================================
 AI FINANCIAL INSIGHTS
 FINANCE ANALYTICS PLATFORM
======================================================*/

document.addEventListener("DOMContentLoaded",function(){

    initializeDashboard();

});

let finance={};

/*=====================================================
 LOAD DATA
======================================================*/

function initializeDashboard(){

    loadFinanceData();

    createBudgetChart();

    createIncomeExpenseChart();

    animateCounters();

    animateHealthScore();

}

/*=====================================================
 JSON
======================================================*/

function loadFinanceData(){

    const json=document.getElementById("finance-data");

    if(!json){

        console.error("Finance data not found");

        return;

    }

    finance=JSON.parse(json.textContent);

}

/*=====================================================
 HEALTH SCORE
======================================================*/

function animateHealthScore(){

    const element=document.querySelector(".health-circle h2");

    if(!element) return;

    let target=parseInt(finance.healthScore);

    let current=0;

    const timer=setInterval(function(){

        current++;

        element.innerHTML=current+"%";

        if(current>=target){

            clearInterval(timer);

        }

    },20);

}

/*=====================================================
 KPI COUNTERS
======================================================*/

function animateCounters(){

    const counters=document.querySelectorAll(".summary-card h3");

    counters.forEach(function(counter){

        let text=counter.innerText;

        let value=parseFloat(text.replace(/[₹,]/g,""));

        if(isNaN(value)) return;

        let current=0;

        let increment=value/60;

        counter.innerHTML="₹0";

        const timer=setInterval(function(){

            current+=increment;

            if(current>=value){

                current=value;

                clearInterval(timer);

            }

            counter.innerHTML="₹"+Math.round(current).toLocaleString();

        },15);

    });

}

/*=====================================================
 BUDGET CHART
======================================================*/

function createBudgetChart(){

    const canvas=document.getElementById("budgetChart");

    if(!canvas) return;

    let used=finance.budgetUsage;

    if(used>100){

        used=100;

    }

    new Chart(canvas,{

        type:"doughnut",

        data:{

            datasets:[{

                data:[

                    used,

                    100-used

                ],

                backgroundColor:[

                    "#4f46e5",

                    "#e5e7eb"

                ],

                borderWidth:0

            }]

        },

        options:{

            responsive:true,

            cutout:"75%",

            plugins:{

                legend:{

                    display:false

                }

            }

        }

    });

}

/*=====================================================
 INCOME VS EXPENSE
======================================================*/

function createIncomeExpenseChart(){

    const canvas=document.getElementById("incomeExpenseChart");

    if(!canvas) return;

    new Chart(canvas,{

        type:"bar",

        data:{

            labels:[

                "Income",

                "Expense",

                "Investment"

            ],

            datasets:[{

                data:[

                    finance.income,

                    finance.expense,

                    finance.investment

                ],

                backgroundColor:[

                    "#10b981",

                    "#ef4444",

                    "#3b82f6"

                ],

                borderRadius:12

            }]

        },

        options:{

            responsive:true,

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

/*=====================================================
 CARD ANIMATION
======================================================*/

const observer=new IntersectionObserver(function(entries){

    entries.forEach(function(entry){

        if(entry.isIntersecting){

            entry.target.style.opacity="1";

            entry.target.style.transform="translateY(0px)";

        }

    });

},{

    threshold:.2

});

document.querySelectorAll(

".summary-card,.panel,.recommendation-card"

).forEach(function(card){

    card.style.opacity="0";

    card.style.transform="translateY(30px)";

    card.style.transition=".6s";

    observer.observe(card);

});

/*=====================================================
 HEALTH COLOR
======================================================*/

window.addEventListener("load",function(){

    const circle=document.querySelector(".health-circle");

    const score=finance.healthScore;

    if(!circle) return;

    if(score>=80){

        circle.style.borderColor="#10b981";

    }

    else if(score>=60){

        circle.style.borderColor="#f59e0b";

    }

    else{

        circle.style.borderColor="#ef4444";

    }

});

/*=====================================================
 HOVER EFFECT
======================================================*/

document.querySelectorAll(".recommendation-card").forEach(function(card){

    card.addEventListener("mouseenter",function(){

        this.style.transform="translateX(8px)";

    });

    card.addEventListener("mouseleave",function(){

        this.style.transform="translateX(0px)";

    });

});

/*=====================================================
 AUTO REFRESH
======================================================*/

setInterval(function(){

    console.log("AI Dashboard Active");

},60000);

