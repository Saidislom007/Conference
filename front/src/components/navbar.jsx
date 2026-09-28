import React from "react";
// Prompt use Tailwindcss
export default function Navbar() {
    return (
        <header className="header">
            <nav className="navbar">
                <div className="logo">
                    <a href=""><img src="https://akadmvd.uz/assets/public/images/footer_logo.png" alt="Logo" /></a>
                </div>
                <ul className="nav-links">
                    <a href="#" className="active">Bosh sahifa</a>
                    <a href="#">Konferensiyalar</a>

                </ul>
            </nav>
        </header>
    );
}