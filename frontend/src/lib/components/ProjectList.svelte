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

    // Props
    export let className="";
    // List of projects that will be shown.
    export let projectNames = [];

    // And fill the array with values from the database.
    fetch(`${import.meta.env.VITE_API_URL}/project/all`)
    .then(res => res.json())
    .then(data => {
        projectNames = [...data.map(project => ({name: project.name, id: project._id}))]
    });

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
</script>

<div class={className}>
    <Input className="searchbar margin0" placeholder="Search For A Project" />
    <ul>
        {#each projectNames as projectName}
            <ListItemWithDelete className="project-name" value={projectName.name} id={projectName.id} deleteFunction={deleteProject}/>
        {/each}
    </ul>
</div>


<style>
    
</style>