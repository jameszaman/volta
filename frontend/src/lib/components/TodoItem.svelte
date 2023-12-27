<script>
    import ListItemWithEditDelete from "./ListItemWithEditDelete.svelte";
    import TodoStatus from "./TodoStatus.svelte";

    export let listItem = {};
    export let editTodo = () => {};
    export let deleteTodo = () => {};
</script>

<div class="flex items-center hover:bg-zinc-800 rounded-lg relative cursor-grab" draggable="true">
    <TodoStatus status={listItem.status} todo_id={listItem["_id"]} />
    <ListItemWithEditDelete
        value={listItem.todo}
        id={listItem["_id"]}
        editFunction={editTodo}
        deleteFunction={deleteTodo}
        className="w-full"
    />
</div>