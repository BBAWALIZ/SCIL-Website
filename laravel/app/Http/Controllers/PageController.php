<?php

namespace App\Http\Controllers;

use App\Support\Catalog;
use Illuminate\Contracts\View\View;

class PageController extends Controller
{
    public function __construct(private Catalog $catalog) {}

    public function home(): View
    {
        $c = $this->catalog;
        $skip = config('scil.home_testimonials_skip');
        $solo = $c->solo();

        return view('pages.home', [
            'stations' => $c->stations(),
            'machines' => $c->machines()->keyBy('id'),
            'counts' => $c->machines()->countBy('station'),
            'testimonials' => $c->testimonials()->reject(fn ($t) => in_array($t['org'], $skip))->values(),
            'logos' => $c->clientLogos(),
            'soloPick' => collect(config('scil.home_solo'))->map(fn ($i) => $solo[$i]),
            'soloCount' => $solo->count(),
        ]);
    }

    public function equipment(): View
    {
        $c = $this->catalog;

        return view('pages.equipment', [
            'stations' => $c->stations(),
            'water' => $c->water(),
            'machines' => $c->machines(),
        ]);
    }

    public function machine(string $slug): View
    {
        $c = $this->catalog;
        $machine = $c->findBySlug($slug) ?? abort(404);

        return view('pages.machine', [
            'm' => $machine,
            'station' => $c->stationMap()[$machine['station']],
            'stations' => $c->stations(),
            'body' => $c->bodyBlocks($machine['body']),
            'specs' => $c->specs($machine['id']),
            'siblings' => $c->machinesIn($machine['station'])->where('id', '!=', $machine['id'])->take(4),
        ]);
    }

    public function services(): View
    {
        return view('pages.services');
    }

    public function about(): View
    {
        return view('pages.about', ['team' => $this->catalog->team()]);
    }

    public function solo(): View
    {
        return view('pages.solo', ['solo' => $this->catalog->solo()]);
    }

    public function contact(): View
    {
        return view('pages.contact');
    }
}
