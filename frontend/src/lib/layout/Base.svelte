<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import TodoList from "../components/TodoList.svelte";

    // Stores
    import { currentProject } from "../../stores/projectStore.js";

    let current_project = "6560e00b3992e65d78333560";
    currentProject.subscribe((value) => current_project = value);

    let todo_list = []

    $: {
        if(current_project) {
            fetch(`${import.meta.env.VITE_API_URL}/todo/all?project_id=${current_project}`)
            .then(res => res.json())
            .then(data => {
                todo_list = data
            });
        }
    }
</script>

<div class="grid justify-items-center col-span-12 md:col-span-11">
    <TodoList bind:todoList={todo_list} />
</div>
