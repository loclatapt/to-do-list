var add_task = document.querySelector(".add_task");
var main_ul = document.querySelector(".all_tasks");

add_task.onclick = function () {
    var main_ul = document.querySelector(".all_tasks");
    var all_tasks = document.querySelector(".all_tasks li");
    var input_text = document.querySelector(".input_text input");
    var i = Math.floor(Math.random() * 67986789);
    if (input_text.value.length > 5) {
        var new_line = document.createElement("li");
        new_line.setAttribute("id", i);
        var list_items = `<hr class="mt-2"><div class="my-4 flex justify-between px-1"><div class="flex items-center gap-2"><span onclick="tick(${i})" class="h-8 cursor-pointer w-8 flex justify-center items-center border border-gray-600 rounded-full "><i id="checked${i}" class="transition-all hover:text-lg text-blue-500 hover:text-blue-900 fa fa-check"></i></span><p class="md:max-w-[375px] truncate max-w-[280px] "><strike id="strike${i}" class="text-gray-600 text-sm no-underline" >${input_text.value}</strike></p></div><span onclick="trash(${i})" class="h-8 cursor-pointer w-8 flex justify-center items-center border border-gray-600 rounded-full "><i class="transition-all hover:text-lg text-red-600 hover:text-red-900 fa fa-trash"></i></span></div>`;
        new_line.innerHTML = list_items;
        main_ul.appendChild(new_line);
        input_text.value = "";
    }
}

function tick(random_id) {
    var striked = document.getElementById("strike" + random_id);
    striked.classList.toggle('no-underline');
}
function trash(random_id) {
    var get_id = document.getElementById(random_id);
    main_ul.removeChild(get_id);
}