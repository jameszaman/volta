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
</script>

<div class={className}>
    <form action="">
        <Input className="searchbar margin0" placeholder="Create a new Project" />
    </form>
</div>


<style>
    * {
        box-sizing: border-box;
    }
    
</style>