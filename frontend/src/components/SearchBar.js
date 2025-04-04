import { useState } from "react";
import { Input } from "@/components/ui";
import { Search } from "lucide-react";

export default function SearchBar({ onSearch }) {
    const [query, setQuery] = useState("");

    const handleSearch = (e) => {
        setQuery(e.target.value);
        onSearch(e.target.value);
    };

    return (
        <div className="p-2 bg-gray-800 rounded-xl flex items-center">
            <Search className="text-gray-400 mr-2" />
            <Input
                type="text"
                placeholder="Search songs..."
                value={query}
                onChange={handleSearch}
                className="bg-transparent text-white border-none focus:ring-0"
            />
        </div>
    );
}