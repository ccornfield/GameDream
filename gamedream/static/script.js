/*document.addEventListener("DOMContentLoaded", function(){
    let buttons = document.getElementById("add_game_title")

    for (let button of buttons) {
        button.addEventListener("click", function() {
            if (this.getAttribute("type") === "create"){
                document.getElementById("add_game_title").outerHTML = 
                `   <div class="mb-3">
                    <label for="title_id">Desired Titles</label>
                    <select id = "title_id"  name="title_id" class="form-select" aria-label="Titles">
                        <option selected>Add Titles Here</option>
                        {% for title in titles%}
                            <option value="{{title.id}}">{{title.game_title}}</option>
                        {% endfor %}
                    </select>
                    </div>`
                document.getElementById("new_button").outerHTML = 
                `<button id="add_game_title" type="create"></button>
                <div id="new_button"></div>
                <br>`
            }
        });
    }
});*/