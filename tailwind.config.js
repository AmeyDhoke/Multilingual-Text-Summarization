/** @type {import('tailwindcss').Config} */
export default {
    content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
    theme: {
        extend: {
            colors: {
                custGrey: "#F4F4F4",
            },
        },
    },
    plugins: [],
};
