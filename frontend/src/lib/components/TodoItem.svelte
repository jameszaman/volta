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

    // Props
    export let listItem = {};
    export let className = "";
    export let isBeingDragged = false;
    export let editTodo = () => {};
    export let deleteTodo = () => {};
    export let dragStart = () => {};

    // Stores
    import { taskItemDraggable } from "../../stores/todoStore.js";

    let draggable = true;
    taskItemDraggable.subscribe((value) => draggable = value);
</script>

<div
    class="flex items-center hover:bg-zinc-800 rounded-lg relative"
    class:cursor-grab={draggable}
    draggable={draggable}
    on:dragstart={dragStart}
    class:opacity-60={isBeingDragged}
    class:bg-zinc-800={isBeingDragged}
    >
    <TodoStatus status={listItem.status} todo_id={listItem["_id"]} />
    <ListItemWithEditDelete
        value={listItem.todo}
        id={listItem["_id"]}
        isLineThrough={listItem.status === "completed"}
        editFunction={editTodo}
        deleteFunction={deleteTodo}
        className={className + " w-full"}
    />
</div>