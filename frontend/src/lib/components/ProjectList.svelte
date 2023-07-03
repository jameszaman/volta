<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import Input from "../components/Input.svelte";

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
</script>

<div class={className}>
    <Input className="searchbar margin0" placeholder="Search For A Project" />
    <ul>
        {#each projectNames as projectName}
            <li class="project-name">
                <a href="#{projectName.name}">{projectName.name}</a>
            </li>
        {/each}
    </ul>
</div>


<style>
    a {
        text-decoration: none;
        color: var(--white);
    }

    a:hover {
        text-decoration: underline;
    }

    .project-name {
        padding: 0.5rem;
    }
</style>