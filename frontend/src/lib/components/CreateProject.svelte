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
    export let projectNames = [];

    let inputValue = "";

    function addProject() {
        if(inputValue) {
            // Make a POST request with necessary parameters to create a new todo.
            fetch(`${import.meta.env.VITE_API_URL}/project/new`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                body: JSON.stringify({
                    "name": inputValue,
                })
            })
            .then(res => res.json())
            .then(todo_id => {
                // Also add the todo to the frontend.
                projectNames = [...projectNames, {"name": inputValue, "id": todo_id}];
            })
        }
    }
</script>

<div class={className + " py-2"}>
    <form on:submit|preventDefault={addProject} action="#">
        <Input bind:value={inputValue} placeholder="Create a new Project" className="w-full rounded outline-none" />
    </form>
</div>

<style>
    * {
        box-sizing: border-box;
    }
    
</style>