<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import Todo from "../components/Todo.svelte";

    // props
    export let current_project = 0


    let todo_list = []

    $: {
        fetch(`${import.meta.env.VITE_API_URL}/todo/all?project_id=${current_project}`)
        .then(res => res.json())
        .then(data => {
            console.log(data);
            todo_list = [...data.map(todo => ({todo: todo.todo, id: todo._id}))]
            console.log
        });
    }
</script>

<div class="main-div">
    <Todo bind:todoList={todo_list}/>
</div>


<style>
    .main-div {
        grid-column: 4/13;
        display: grid;
        justify-items: center;
    }

    
    @media (max-width: 768px) {
        .main-div {
            grid-column: 1/13;
        }
    }
</style>