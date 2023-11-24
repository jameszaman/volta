<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import TodoList from "../components/TodoList.svelte";

    // props
    export let current_project = 0;

    let todo_list = []

    $: {
        fetch(`${import.meta.env.VITE_API_URL}/todo/all?project_id=${current_project}`)
        .then(res => res.json())
        .then(data => {
            todo_list = data
        });
    }
</script>

<div class="grid justify-items-center col-span-12 md:col-span-11">
    <TodoList bind:todoList={todo_list} bind:current_project={current_project}/>
</div>
