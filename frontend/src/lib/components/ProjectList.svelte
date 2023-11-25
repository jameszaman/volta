<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import Input from "../components/Input.svelte";
    import ListItemWithDelete from "./ListItemWithDelete.svelte";

    // Store
    import { currentProject } from "../../stores/projectStore.js";
    import { onMount } from "svelte";
    import Icon from "@iconify/svelte";

    // Props
    export let className="";
    // List of projects that will be shown.
    export let projectNames = [];

    // Functions for this component.
    function deleteProject(id) {
        // Make a DELETE request with necessary parameters to delete a todo.
        fetch(`${import.meta.env.VITE_API_URL}/project/delete?id=${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Accept": "*/*",
            }
        })
        .then(res => res.json())
        .then(data => {
            // Also remove the todo from the frontend.
            projectNames = projectNames.filter(projectName => {
                return projectName.id != id
            })
        })
    }

    function changeProject(id) {
        // Change the current project with the id of whichever project was clicked.
        currentProject.set(id);
    }

    onMount(() => {
        // And fill the array with values from the database.
        fetch(`${import.meta.env.VITE_API_URL}/project/all`)
        .then(res => res.json())
        .then(data => {
            projectNames = [...data.map(project => ({name: project.name, id: project._id}))]
            // Set the current project to the first project in the list.
            currentProject.set(projectNames[0].id)
        });
    })
</script>

<div class={className + " pt-2 max-h-[510px] md:max-h-[830px] flex flex-col"}>
    <Input placeholder="Search For A Project" className="w-full rounded outline-none mb-1" />
    <ul class="max-h-full overflow-y-auto">
        {#each projectNames as projectName}
            <li class="flex items-center hover:bg-zinc-800 rounded-lg pl-2">
                <Icon icon="mdi:folder" class="text-xl" />
                <ListItemWithDelete click={() => {changeProject(projectName.id)}} className="w-full hover:underline rounded-lg cursor-pointer" value={projectName.name} id={projectName.id} deleteFunction={deleteProject} />
            </li>
        {/each}
    </ul>
</div>
