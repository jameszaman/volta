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
    import { currentlyDraggingTodoIndex, currentDragPosition } from "../../stores/todoStore";

    // Subscribing to stores.
    let current_project = "6560e00b3992e65d78333560"; // ! This should be dynamic...
    currentProject.subscribe((value) => current_project = value);
    // This is the index of the task we are dragging.
    let itemDraggingIndex;
    // When we are dragging the task, we want to keep track of where we have the task currently.
    // This is to show that beautiful animation of the task moving.
    let dragOverIndex;
    currentlyDraggingTodoIndex.subscribe((value) => {
        itemDraggingIndex = value
        dragOverIndex = value;
    });

    // Declaring necessary variables.
    let todo_list = []

    $: {
        // Whenever the project changes, we wish to show the todo of which ever is the current project.
        if(current_project) {
            fetch(`${import.meta.env.VITE_API_URL}/todo/all?project_id=${current_project}`)
            .then(res => res.json())
            .then(data => {
                todo_list = data
            });
        }
    }

    // This function is for handling when a task is placed in a new position.
    function handleDrop(event) {
        event.preventDefault();
        let droppedElementIndex = getElementToSwitch(event.currentTarget, event.clientY);
        // Handling the case when the task is dropped at the end of the list.
        if(droppedElementIndex === undefined) {
            droppedElementIndex = todo_list.length - 1;
        }
        // When the task is dropped we make a request at the backend to update the position of the task.
        if (itemDraggingIndex !== null) {
            fetch(`${import.meta.env.VITE_API_URL}/todo/update_todo_position`, {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    project_id: current_project,
                    previous_position: itemDraggingIndex,
                    new_position: droppedElementIndex,
                }),
            })
            .catch((err) => {
                console.error(err);
            });
        }
    }

    // This function is for handling when a todo has stopped dragging in anyway.
    function handleDragEnd(event) {
        // We are currently not dragging any item.
        currentlyDraggingTodoIndex.set(null);
        currentDragPosition.set(null);
    }

    function getElementToSwitch(container, y) {
        // Get all the elements. [P.S. I had thought of a way without selecting like this but forgot later on. I encourage you to try to find a way without selecting like this.]
        const draggableElements = container.querySelectorAll("li");
        
        // We are using the current mouse position (y) and compare it with the position of all the elements to find whichever is closest.
        return [...draggableElements].reduce((closest, child, index) => {
        const box = child.getBoundingClientRect();
        const offset = box.bottom - y; // y is the mouse position. Offset is distance from element to mouse position.
        if (offset > 0 && offset < closest.offset) {
            return { offset: offset, element: child , index};
        } else {
            return closest;
        }
        }, { offset: Number.POSITIVE_INFINITY }).index;
    }

    function handleDragOver(event) {
        event.preventDefault();
        let droppedOverIndex = getElementToSwitch(event.currentTarget, event.clientY);
        // Handling the case when the task is dropped outside the list.
        if(!droppedOverIndex) {
            if(dragOverIndex === 1) {
                droppedOverIndex = 0;
            }
            else return
        }
        // If dropped inside the list then we switch the tasks.
        if (dragOverIndex !== null && droppedOverIndex !== dragOverIndex) {
            // Switching the tasks.
            const itemToChange = todo_list[dragOverIndex];
            todo_list.splice(dragOverIndex, 1);
            todo_list.splice(droppedOverIndex, 0, itemToChange);
            todo_list = todo_list;

            // We are keeping track of the last position of the task while dragging.
            dragOverIndex = droppedOverIndex;
            currentDragPosition.set(dragOverIndex);
        }
        return;
    }

    function handleDragLeave(event) {
        event.preventDefault();
    }

</script>

<div class="grid justify-items-center col-span-12 md:col-span-11">
    <TodoList bind:todoList={todo_list}
        dragDrop={handleDrop}
        dragEnd={handleDragEnd}
        dragLeave={handleDragLeave}
        dragOver={handleDragOver}
    />
</div>
