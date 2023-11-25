<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
  import Icon from "@iconify/svelte";
</script>

<nav class="flex justify-between items-center px-5 border-b border-gray-700 col-span-12">
    <div>
        Volta
    </div>
    <div class="w-3/4 lg:w-1/2 flex">
        <div class="bg-emerald-400 rounded-l flex justify-center items-center px-3">
            <Icon icon="gala:search" class="text-3xl text-zinc-800" />
        </div>
        <input type="text" class="px-3 py-1 w-full text-lg rounded-r outline-none" placeholder="Search...">
    </div>
    <div>
        <!-- Will hold dropdown in the future if needed. -->
    </div>
</nav>
