<script>
    import Input from "../components/Input.svelte";

    let projectNames = []

    // And fill the array with values from the database.
    fetch(`${import.meta.env.VITE_API_URL}/project/all`)
    .then(res => res.json())
    .then(data => {
        projectNames = [...data.map(project => ({name: project.name, id: project._id}))]
    });
</script>

<nav>
    <div>
        Project List
    </div>
    <Input className="searchbar" placeholder="Search For A Project" />
    <ul>
        {#each projectNames as projectName}
            <li class="project-name">
                <a href="#{projectName.name}">{projectName.name}</a>
            </li>
        {/each}
        
    </ul>
</nav>

<style>
    nav {
        background-color: var(--dark4);
        display: flex;
        flex-direction: column;
        grid-column: 1/4;
    }

    .project-name {
        padding: 0.5rem;
    }

    a {
        text-decoration: none;
        color: var(--white);
    }

    a:hover {
        text-decoration: underline;
    }

    @media (max-width: 768px) {
        nav {
            grid-column: 1/13;
        }
    }
</style>