<?php

namespace App\Support;

use Illuminate\Support\Collection;

/**
 * Puts the language-neutral facts in config/scil.php together with the
 * words for the current language in lang/{locale}/*.php.
 *
 * When the back end arrives, this is the one class to point at the
 * database instead of the files. The views do not need to change.
 */
class Catalog
{
    /** The six line stations, in order, for the current language. */
    public function stations(): Collection
    {
        return collect(config('scil.stations'))->map(fn (array $s, string $key) => $this->station($key, $s))->values();
    }

    /** Station 00, water treatment. */
    public function water(): array
    {
        $w = config('scil.water');

        return $this->station($w['key'], $w);
    }

    /** All stations including water treatment, keyed by station key. */
    public function stationMap(): Collection
    {
        return $this->stations()->push($this->water())->keyBy('key');
    }

    /** Every machine, in catalogue order. */
    public function machines(): Collection
    {
        return collect(config('scil.machines'))->map(fn (array $m, int $id) => $this->machine($id, $m))->values();
    }

    public function machinesIn(string $station): Collection
    {
        return $this->machines()->where('station', $station)->values();
    }

    public function machine(int $id, ?array $m = null): array
    {
        $m ??= config("scil.machines.$id");
        $t = trans("machines.$id");

        return [
            'id' => $id,
            'slug' => $m['slug'],
            'station' => $m['station'],
            'image' => $m['image'],
            'name' => $t['name'],
            'fig' => $t['fig'],
            'summary' => $t['summary'],
            'body' => $t['body'] ?? [],
        ];
    }

    public function findBySlug(string $slug): ?array
    {
        return $this->machines()->firstWhere('slug', $slug);
    }

    /**
     * Turns the body lines into blocks for the view:
     * "-text" is a list item, "#text" a sub-heading, anything else a paragraph.
     */
    public function bodyBlocks(array $lines): array
    {
        $blocks = [];
        foreach ($lines as $line) {
            if (str_starts_with($line, '-')) {
                $last = array_key_last($blocks);
                if ($last !== null && $blocks[$last]['type'] === 'list') {
                    $blocks[$last]['items'][] = substr($line, 1);
                } else {
                    $blocks[] = ['type' => 'list', 'items' => [substr($line, 1)]];
                }
            } elseif (str_starts_with($line, '#')) {
                $blocks[] = ['type' => 'heading', 'text' => substr($line, 1)];
            } else {
                $blocks[] = ['type' => 'p', 'text' => $line];
            }
        }

        return $blocks;
    }

    /** The published specification table for a machine, with translated labels. */
    public function specs(int $id): ?array
    {
        $s = config("scil.specs.$id");
        if (! $s) {
            return null;
        }
        $label = fn (string $l) => trans()->has("specs.$l") ? trans("specs.$l") : $l;

        return [
            'caption' => $label($s['caption']),
            'head' => isset($s['head']) ? array_map($label, $s['head']) : null,
            'rows' => isset($s['head'])
                ? $s['rows']
                : array_map(fn ($r) => [$label($r[0]), $r[1]], $s['rows']),
        ];
    }

    /** SOLO fixed-price machines. */
    public function solo(): Collection
    {
        $words = trans('solo');

        return collect(config('scil.solo'))->map(function (array $s, int $i) use ($words) {
            $w = $words[$i];

            return [
                'index' => $i,
                'image' => $s['image'],
                'station' => $s['station'],
                'name' => $w['name'],
                'desc' => $w['desc'],
                'prices' => array_map(null, $w['labels'], $s['prices']),
            ];
        });
    }

    public function testimonials(): Collection
    {
        return collect(trans('testimonials'))->map(fn (array $t, string $org) => $t + ['org' => $org])->values();
    }

    public function team(): Collection
    {
        $roles = trans('team.roles');
        $names = trans('team.names');

        return collect(config('scil.team'))->map(fn (array $p) => [
            'image' => $p['image'],
            'name' => $names[$p['name']] ?? $p['name'],
            'name_zh' => $p['name_zh'],
            'role' => $roles[$p['role']] ?? $p['role'],
        ]);
    }

    /** Client logo files, read from public/assets/img/clients. */
    public function clientLogos(): array
    {
        $files = glob(public_path('assets/img/clients/*.{png,jpg,jpeg,svg,webp}'), GLOB_BRACE) ?: [];
        $names = array_map('basename', $files);
        sort($names);

        return $names;
    }

    private function station(string $key, array $s): array
    {
        $t = trans("stations.$key");

        return [
            'key' => $key,
            'no' => $s['no'],
            'token' => $s['token'],
            'name' => $t['name'],
            'out' => $t['out'],
            'short' => $t['short'],
            'text' => $t['text'],
        ];
    }
}
