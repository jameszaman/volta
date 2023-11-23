<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    // Props
    export let placeholder="";
    export let value="";
    export let className="";
</script>

<input type="text" {placeholder} bind:value={value} class={className + " px-2 py-1"}>
