

document.querySelectorAll(".flash").forEach(flash=>{

    setTimeout(()=>{

        flash.style.opacity="0";

        flash.style.transform="translateX(40px)";

        setTimeout(()=>{

            flash.remove();

        },300);

    },4000);

});

document.querySelectorAll(".flash-close").forEach(button=>{

    button.addEventListener("click",()=>{

        button.closest(".flash").remove();

    });

});

