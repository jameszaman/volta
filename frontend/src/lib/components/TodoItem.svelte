<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import ListItemWithEditDelete from "./ListItemWithEditDelete.svelte";
    import TodoStatus from "./TodoStatus.svelte";

    export let listItem = {};
    export let editTodo = () => {};
    export let deleteTodo = () => {};
    export let dragStart = () => {};
</script>

<div
    class="flex items-center hover:bg-zinc-800 rounded-lg relative cursor-grab"
    draggable="true"
    on:dragstart={dragStart}
    >
    <TodoStatus status={listItem.status} todo_id={listItem["_id"]} />
    <ListItemWithEditDelete
        value={listItem.todo}
        id={listItem["_id"]}
        editFunction={editTodo}
        deleteFunction={deleteTodo}
        className="w-full"
    />
</div>