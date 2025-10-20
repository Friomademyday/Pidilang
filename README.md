<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PIDILANG: The Language of the People</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'pidi-primary': '#FACC15',
                        'pidi-secondary': '#4F46E5',
                        'pidi-bg': '#10172A',
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                }
            }
        }
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
        .pidi-code {
            background-color: #1F2937;
            border-left: 4px solid #4F46E5;
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            font-family: monospace;
            white-space: pre;
        }
        .pidi-table th, .pidi-table td {
            border-bottom: 1px solid #374151;
            padding: 0.75rem 0.5rem;
            text-align: left;
        }
        .pidi-table th {
            color: #FACC15;
            font-weight: 700;
            text-transform: uppercase;
        }
        .pidi-table tr:last-child td {
            border-bottom: none;
        }
    </style>
</head>
<body class="bg-pidi-bg text-gray-200 min-h-screen font-sans p-6 md:p-12">

    <div class="max-w-4xl mx-auto">
        
        <header class="text-center mb-12">
            <h1 class="text-6xl md:text-8xl font-black text-pidi-primary leading-tight tracking-tighter">PIDILANG</h1>
            <h2 class="text-2xl md:text-3xl font-semibold text-gray-300 mt-2">🗣️ Code Wey Sabi Talk. No Be Mumu Talk.</h2>
            <div class="w-full h-1 bg-pidi-secondary mt-6 rounded-full"></div>
        </header>

        <section class="mb-12">
            <h3 class="text-3xl font-bold text-pidi-primary mb-4 border-b border-pidi-secondary pb-2">😤 Background: Wetin Dey Vex Me</h3>
            <p class="text-lg leading-relaxed mb-4">
                Look, enough is enough! We don tire for all these **oyinbo** languages—the Javascript wey dey vex, the Python wey too calm, the Java wey be like long essay. All of them just dey make code confusing like traffic for Lagos.
            </p>
            <p class="text-lg leading-relaxed mb-4">
                We need something simple, sharp, and wey get soul!
            </p>
            <p class="text-lg leading-relaxed">
                PidiLang (Pidgin Language) na the answer! We no come to play; we come to **CHOP** the system. This na a high-level, dynamically-typed language where your code go feel like you dey send your junior brother go market. Direct, no long story, and every command get sense!
            </p>
            <p class="text-xl font-bold italic text-pidi-secondary mt-6">
                If you fit talk Pidgin, you fit code PidiLang.
            </p>
        </section>

        <section class="mb-12">
            <h3 class="text-3xl font-bold text-pidi-primary mb-4 border-b border-pidi-secondary pb-2">✨ The Gist: Core Keywords</h3>
            <div class="overflow-x-auto rounded-lg shadow-xl">
                <table class="w-full text-sm pidi-table">
                    <thead>
                        <tr>
                            <th class="py-3 px-4">PidiLang Keyword</th>
                            <th class="py-3 px-4">Wetin E Mean</th>
                            <th class="py-3 px-4">Programming Purpose</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td><code class="text-pidi-primary font-bold">DAT_ME</code></td><td>That's Me / This Is</td><td>Variable Declaration</td></tr>
                        <tr><td><code class="text-pidi-primary font-bold">TALK_AM</code></td><td>Talk It</td><td>Print to Console</td></tr>
                        <tr><td><code class="text-pidi-primary font-bold">DO_WORK</code></td><td>Do Work</td><td>Define a Function</td></tr>
                        <tr><td><code class="text-pidi-primary font-bold">IF_E_TRUE</code></td><td>If It Is True</td><td>Conditional Check (if)</td></tr>
                        <tr><td><code class="text-pidi-primary font-bold">WAKA_ROUND</code></td><td>Walk Around</td><td>Iterating/Looping (for)</td></tr>
                        <tr><td><code class="text-pidi-primary font-bold">IF_NO_WAHALA</code></td><td>If No Trouble</td><td>Successful Exit/Stop Run</td></tr>
                    </tbody>
                </table>
            </div>

            <h4 class="text-2xl font-bold text-gray-300 mt-8 mb-3">🛑 No More Wahala: The Grand Finale</h4>
            <p class="text-lg leading-relaxed">
                When your code run finish and everything dey fine, you just call <code class="bg-gray-700 text-pidi-primary p-1 rounded-md">IF_NO_WAHALA</code>. No error, no confusion, just a clean exit. It’s like saying, *"Ah, thank God, we made it!"*
            </p>
        </section>

        <section class="mb-12">
            <h3 class="text-3xl font-bold text-pidi-primary mb-4 border-b border-pidi-secondary pb-2">📝 Sample Code: Market Teller v1.1</h3>
            <p class="text-lg leading-relaxed mb-4">
                See how simple the logic flows when we code PidiLang. No need to stress your brain trying to remember *def* or *return*.
            </p>
            <pre class="pidi-code text-white">
<span class="text-gray-500">// WETIN BE DIS: The Market Teller Script
// We go check if the customer get enough money</span>

<span class="text-pidi-primary">DAT_ME</span> item_price = 500
<span class="text-pidi-primary">DAT_ME</span> customer_cash = 750

<span class="text-pidi-primary">DO_WORK</span> calculate_change(cash, cost):
    <span class="text-pidi-primary">DAT_ME</span> change = cash - cost
    <span class="text-pidi-primary">GIVE_BACK</span> change

<span class="text-pidi-primary">TALK_AM</span> "Welcome to AuraMart, Oga!"

<span class="text-pidi-primary">IF_E_TRUE</span> (customer_cash >= item_price):
    <span class="text-pidi-primary">TALK_AM</span> "You get enough money. Thank you!"
    <span class="text-pidi-primary">DAT_ME</span> customer_change = calculate_change(customer_cash, item_price)
    <span class="text-pidi-primary">TALK_AM</span> "Your change na: " + customer_change + " Naira."
    <span class="text-pidi-primary">TALK_AM</span> "Come back o!"
    <span class="text-pidi-primary">IF_NO_WAHALA</span> <span class="text-gray-500">// Everything don settle, program go close.</span>
<span class="text-pidi-primary">ELSE_IF_NO</span>:
    <span class="text-pidi-primary">TALK_AM</span> "Oga, your money no reach o. Sorry! No vex."

<span class="text-pidi-primary">DAT_ME</span> my_team = PLENTY_THINGS ["Bisi", "Chinedu", "Aisha"]
<span class="text-pidi-primary">TALK_AM</span> " "
<span class="text-pidi-primary">TALK_AM</span> "Team wey dey WAKA:"
<span class="text-pidi-primary">WAKA_ROUND</span> member IN my_team:
    <span class="text-pidi-primary">TALK_AM</span> "Team member: " + member + " dey available!"
</pre>
        </section>

        <section class="mb-12">
            <h3 class="text-3xl font-bold text-pidi-primary mb-4 border-b border-pidi-secondary pb-2">🛠️ Setup: How To Start The Engine</h3>
            <p class="text-lg leading-relaxed mb-4">
                To run PidiLang, you just need to get the **PidiCompiler** (coming soon!):
            </p>
            <ol class="list-decimal list-inside space-y-3 text-lg leading-relaxed">
                <li><strong class="text-pidi-secondary">Download:</strong> Go find the latest compiler for your system (Linux, Windows, or Mac).</li>
                <li><strong class="text-pidi-secondary">Make Sabi:</strong> Add the compiler executable to your system PATH so your shell fit **sabi** where e dey.</li>
                <li><strong class="text-pidi-secondary">Run Am:</strong> Open your terminal and type:</li>
            </ol>
            <pre class="bg-gray-700 text-white p-4 rounded-lg mt-4 text-base shadow-lg">
<code class="text-green-400">$</code> pidi run my_program.pidi
            </pre>
            <p class="text-lg leading-relaxed mt-4">
                ...and watch your code begin to **WAKA** (walk)!
            </p>
        </section>

        <section class="mb-12">
            <h3 class="text-3xl font-bold text-pidi-primary mb-4 border-b border-pidi-secondary pb-2">🤝 Community: Join The Movement!</h3>
            <p class="text-lg leading-relaxed mb-4">
                We need serious developers who **sabi** Pidgin and who are tired of regular English programming. Let’s make PidiLang the number one language for the hustle! Send us your ideas for new commands.
            </p>
            <h4 class="text-2xl font-bold text-gray-300 mt-6 mb-3">Potential Future Commands:</h4>
            <ul class="list-disc list-inside space-y-2 text-lg ml-4">
                <li><code class="bg-gray-700 text-yellow-300 p-1 rounded-md">WAIT_SMALL</code>: For asynchronous calls.</li>
                <li><code class="bg-gray-700 text-yellow-300 p-1 rounded-md">TRY_LUCK</code>: For error handling (which we now have as <code class="bg-gray-700 text-yellow-300 p-1 rounded-md">TRY_YOUR_BEST</code>!).</li>
                <li><code class="bg-gray-700 text-yellow-300 p-1 rounded-md">MUMU_CHECK</code>: Assertions and validation.</li>
            </ul>
        </section>

        <footer class="text-center pt-8 border-t border-gray-700">
            <p class="text-sm italic text-gray-500">
                NOTE: This README was written by a genuine human being who has, at some point, suffered under the tyranny of excessive semicolons. <strong class="text-red-400">No AI was involved in the composition of this document.</strong>
            </p>
            <p class="text-xl font-bold text-pidi-secondary mt-2">— God bless your hustle!</p>
        </footer>

    </div>

</body>
</html>
