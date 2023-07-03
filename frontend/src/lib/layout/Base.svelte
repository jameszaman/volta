<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import Todo from "../components/Todo.svelte";
</script>

<div class="main-div">
    <Todo />
</div>


<style>
    .main-div {
        grid-column: 4/13;
        display: grid;
        justify-items: center;
    }

    
    @media (max-width: 768px) {
        .main-div {
            grid-column: 1/13;
        }
    }
</style>